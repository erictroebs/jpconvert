from typing import Dict

from ..operations import MapCell


class SetReadonly(MapCell):
    def map_cell(self, cell: Dict) -> Dict:
        # set all markdown cells to readonly
        if cell['cell_type'] != 'code':
            cell['metadata']['editable'] = False

        # find practice macro
        practice = False
        readonly = False

        for line in cell['source']:
            line = line.strip()

            if line == '#jp-practice':
                practice = True
            elif line in ['#jp-practice-ro', '#jp-readonly']:
                readonly = True

        # set readonly
        if not practice or readonly:
            cell['metadata']['editable'] = False

        return cell
