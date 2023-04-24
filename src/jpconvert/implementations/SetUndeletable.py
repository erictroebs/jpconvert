from nbformat import NotebookNode

from ..operations import MapCell


class SetUndeletable(MapCell):
    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        cell['metadata']['deletable'] = False
        return cell
