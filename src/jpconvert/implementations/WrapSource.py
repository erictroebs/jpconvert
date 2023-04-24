from nbformat import NotebookNode

from ..operations import MapCell


class SplitSource(MapCell):
    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        cell['source'] = cell['source'].split('\n')
        return cell


class JoinSource(MapCell):
    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        cell['source'] = '\n'.join(cell['source'])
        return cell
