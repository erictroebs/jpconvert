from nbformat import NotebookNode

from ..operations import MapCell


class SetReadonly(MapCell):
    def __init__(self, force: bool):
        self._force: bool = force

    def map_cell(self, cell: NotebookNode) -> NotebookNode:
        # set all markdown cells to readonly
        if cell['cell_type'] != 'code':
            cell['metadata']['editable'] = False
            return cell

        # find practice macro
        practice = False
        readonly = False

        if 'metadata' in cell and 'tags' in cell['metadata']:
            for tag in cell['metadata']['tags']:
                if tag == 'jp-practice':
                    practice = True
                elif tag in ['jp-practice-ro', 'jp-readonly']:
                    readonly = True

        for line in cell['source']:
            line = line.strip()

            if line in ['#jp-practice', '--jp-practice']:
                practice = True
            elif line in ['#jp-practice-ro', '--jp-practice-ro', '#jp-readonly', '--jp-readonly']:
                readonly = True

        # set readonly
        if (not practice and self._force) or readonly:
            cell['metadata']['editable'] = False

        return cell
