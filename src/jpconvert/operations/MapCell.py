from typing import Dict, Optional

from . import Operation


class MapCell(Operation):
    def __call__(self, cell: Dict) -> Optional[Dict]:
        return self.map_cell(cell)

    def map_cell(self, cell: Dict) -> Dict:
        raise NotImplementedError
