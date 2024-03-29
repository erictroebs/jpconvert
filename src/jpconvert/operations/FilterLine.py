from nbformat import NotebookNode

from . import MapCell


class FilterLine(MapCell):
    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        i = 0
        while i < len(cell['source']):
            if self.filter_line(cell['source'][i]):
                i += 1
            else:
                del cell['source'][i]

        return cell

    def filter_line(self, line: str) -> bool:
        raise NotImplementedError
