from typing import Dict

from ..operations import MapCell


class RemoveTrailingLines(MapCell):
    def map_cell(self, cell: Dict) -> Dict:
        while len(cell['source']) > 0 and cell['source'][-1] in ('', '\n'):
            del cell['source'][-1]

        if len(cell['source']) > 0 and cell['source'][-1].endswith('\n'):
            cell['source'][-1] = cell['source'][-1][:-1]

        return cell
