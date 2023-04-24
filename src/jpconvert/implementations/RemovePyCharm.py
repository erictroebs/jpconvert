from nbformat import NotebookNode

from ..operations import MapCell


class RemovePyCharm(MapCell):
    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        if 'pycharm' in cell['metadata']:
            del cell['metadata']['pycharm']

        return cell
