from typing import List

from nbformat import NotebookNode

from .operations import Operation


class Pipeline:
    def __init__(self):
        self._ops: List[Operation] = []

    def add(self, op: Operation):
        self._ops.append(op)

    def run(self, file: NotebookNode, remove_toolbar: bool = True) -> NotebookNode:
        # remove tag bar
        if remove_toolbar and 'celltoolbar' in file['metadata']:
            del file['metadata']['celltoolbar']

        # map and filter cells
        i = 0
        while i < len(file['cells']):
            cell: NotebookNode = file['cells'][i]

            for op in self._ops:
                cell = op(cell)
                if cell is None:
                    del file['cells'][i]
                    break
            else:
                file['cells'][i] = cell
                i += 1

        # run exit functions
        for op in reversed(self._ops):
            op.exit()

        # return data
        return file
