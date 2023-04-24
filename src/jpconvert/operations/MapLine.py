from nbformat import NotebookNode

from . import MapCell


class MapLine(MapCell):
    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        i = 0
        while i < len(cell['source']):
            cell['source'][i] = self.map_line(cell['source'][i])
            i += 1

        return cell

    def map_line(self, line: str) -> str:
        raise NotImplementedError
