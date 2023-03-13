from typing import Dict

from ..operations import MapCell


class RemovePyCharm(MapCell):
    def map_cell(self, cell: Dict):
        if 'pycharm' in cell['metadata']:
            del cell['metadata']['pycharm']

        return cell
