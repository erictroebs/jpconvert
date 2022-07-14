from typing import Dict

from ..operations import FilterCell


class RemoveCellByMacro(FilterCell):
    def __init__(self, practice: bool, solution: bool, teaching: bool, remove_without_macros: bool):
        self._practice: bool = practice
        self._solution: bool = solution
        self._teaching: bool = teaching
        self._remove_without_macros: bool = remove_without_macros

    def filter_cell(self, cell: Dict) -> bool:
        if not self._practice and not self._solution and not self._teaching:
            return True

        # filter cells without code
        if cell['cell_type'] != 'code':
            return True

        # find macros
        practice = False
        solution = False
        teaching = False

        for line in cell['source']:
            line = line.strip()

            if line in ['#jp-practice', '#jp-practice-ro']:
                practice = True
            elif line == '#jp-solution':
                solution = True
            elif line == '#jp-teaching':
                teaching = True

        # remove cell
        return ((practice and self._practice) or
                (solution and self._solution) or
                (teaching and self._teaching) or
                (not practice and not solution and not teaching and not self._remove_without_macros))
