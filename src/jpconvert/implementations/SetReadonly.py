from typing import Dict

from ..operations import MapCell


class SetReadonly(MapCell):
    def map_cell(self, cell: Dict) -> Dict:
        # set all markdown cells to readonly
        if cell['cell_type'] != 'code':
            cell['metadata']['editable'] = False

        # find practice macro
        practice = False

        for line in cell['source']:
            if line.strip() == '#jp-practice':
                practice = True

        # set readonly
        if not practice:
            cell['metadata']['editable'] = False

        return cell
