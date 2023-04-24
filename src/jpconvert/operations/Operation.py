from typing import Optional

from nbformat import NotebookNode


class Operation:
    def __call__(self, cell: NotebookNode) -> Optional[NotebookNode]:
        raise NotImplementedError

    def exit(self):
        pass
