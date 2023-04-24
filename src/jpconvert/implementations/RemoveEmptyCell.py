from nbformat import NotebookNode

from ..operations import FilterCell


class RemoveEmptyCell(FilterCell):
    def filter_cell(self, cell: NotebookNode) -> bool:
        return len(cell['source']) > 0 and cell['source'] != ['']
