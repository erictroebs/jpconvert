from typing import Dict, Optional

from . import Operation


class FilterCell(Operation):
    def __call__(self, cell: Dict) -> Optional[Dict]:
        return cell if self.filter_cell(cell) else None

    def filter_cell(self, cell: Dict) -> bool:
        raise NotImplementedError
