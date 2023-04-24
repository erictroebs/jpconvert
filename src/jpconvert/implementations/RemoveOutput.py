from nbformat import NotebookNode

from ..operations import MapCell


class RemoveOutput(MapCell):
    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        if cell['cell_type'] != 'code':
            return cell

        if 'execution_count' in cell:
            cell['execution_count'] = None
        if 'outputs' in cell:
            cell['outputs'] = []

        return cell
