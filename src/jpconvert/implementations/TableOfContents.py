import re
from typing import Dict, List, Tuple

from ..operations import FilterCell


class TableOfContents(FilterCell):
    def __init__(self):
        self._cells: List[Tuple[Dict, int, int]] = []
        self._entries: List[Tuple[int, str]] = []

    def filter_cell(self, cell: Dict) -> bool:
        # skip empty cells
        if 'source' not in cell or len(cell['source']) == 0:
            return True

        # find jp-toc macros
        match = re.match(r'^#jp-toc((<|<=|==|>=|>)(\d+)((<|<=|==|>=|>)(\d+))?)?$', cell['source'][0].strip())
        if match is not None:
            _, fc, fv, _, sc, sv = match.groups()

            # parse conditions
            min_level = 1
            max_level = 10

            for c, v in (fc, fv), (sc, sv):
                if c == '<':
                    max_level = int(v) - 1
                elif c == '<=':
                    max_level = int(v)
                elif c == '==':
                    min_level = int(v)
                    max_level = int(v)
                elif c == '>=':
                    min_level = int(v)
                elif c == '>':
                    min_level = int(v) + 1

            cell['source'].append('do not remove during `RemoveEmpty`')
            self._cells.append((cell, min_level, max_level))

        # do not look for headlines in anything other than markdown cells
        if cell['cell_type'] != 'markdown':
            return True

        # find headlines
        for line in cell['source']:
            match = re.match(r'^(#+) (.*)$', line)
            if match is not None:
                level = len(match.group(1))
                title = match.group(2).strip()

                self._entries.append((level, title))

        return True

    def exit(self):
        for cell, min_level, max_level in self._cells:
            # create a list of levels
            levels = []

            for level, _ in self._entries:
                if level not in levels and min_level <= level <= max_level:
                    levels.append(level)

            levels.sort()

            # create toc
            cell['source'] = [f'{"#" * min_level} Inhaltsverzeichnis\n']

            for level, title in self._entries:
                if level in levels:
                    indent = ' ' * (levels.index(level) * 2)
                    anchor = title.replace(' ', '-')
                    anchor = re.sub(r'[^A-Za-z0-9ÄÖÜäöüß-]', '', anchor)

                    cell['source'].append(f'{indent}- [{title}](#{anchor})\n')

            # remove last newline
            if cell['source'][-1].endswith('\n'):
                cell['source'][-1] = cell['source'][-1][:-1]
