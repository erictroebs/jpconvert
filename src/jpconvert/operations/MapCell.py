from typing import Optional

from nbformat import NotebookNode

from . import Operation


class MapCell(Operation):
    def __call__(self, cell: NotebookNode) -> Optional[NotebookNode]:
        return self.map_cell(cell)

    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        raise NotImplementedError
