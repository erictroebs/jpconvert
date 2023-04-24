from typing import Optional

from nbformat import NotebookNode

from . import Operation


class FilterCell(Operation):
    def __call__(self, cell: NotebookNode) -> Optional[NotebookNode]:
        return cell if self.filter_cell(cell) else None

    def filter_cell(self, cell: NotebookNode) -> bool:
        raise NotImplementedError
