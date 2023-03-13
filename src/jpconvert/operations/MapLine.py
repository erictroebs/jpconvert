from typing import Dict

from . import MapCell


class MapLine(MapCell):
    def map_cell(self, cell: Dict) -> Dict:
        i = 0
        while i < len(cell['source']):
            cell['source'][i] = self.map_line(cell['source'][i])
            i += 1

        return cell

    def map_line(self, line: str) -> str:
        raise NotImplementedError
