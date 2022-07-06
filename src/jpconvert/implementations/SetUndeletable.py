from typing import Dict

from ..operations import MapCell


class SetUndeletable(MapCell):
    def map_cell(self, cell: Dict) -> Dict:
        cell['metadata']['deletable'] = False
        return cell
