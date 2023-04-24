from nbformat import NotebookNode

from ..operations import MapCell


class RemoveTrailingLines(MapCell):
    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        while len(cell['source']) > 0 and cell['source'][-1] == '':
            del cell['source'][-1]

        return cell
