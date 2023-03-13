from typing import Dict

from ..operations import FilterCell


class RemoveEmptyCell(FilterCell):
    def filter_cell(self, cell: Dict) -> bool:
        return len(cell['source']) > 0
