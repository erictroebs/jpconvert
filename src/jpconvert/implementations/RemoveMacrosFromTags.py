from nbformat import NotebookNode

from ..operations import MapCell


class RemoveMacrosFromTags(MapCell):
    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        if 'metadata' in cell and 'tags' in cell['metadata']:
            cell['metadata']['tags'] = [t for t in cell['metadata']['tags'] if not t.startswith('jp-')]

        return cell
