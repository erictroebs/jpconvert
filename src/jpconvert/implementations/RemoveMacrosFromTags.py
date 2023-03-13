from typing import Dict

from ..operations import MapCell


class RemoveMacrosFromTags(MapCell):
    def map_cell(self, cell: Dict) -> Dict:
        if 'metadata' in cell and 'tags' in cell['metadata']:
            cell['metadata']['tags'] = [t for t in cell['metadata']['tags'] if not t.startswith('jp-')]

        return cell
