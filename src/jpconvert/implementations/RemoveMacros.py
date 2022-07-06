from ..operations import FilterLine


class RemoveMacros(FilterLine):
    def filter_line(self, line: str) -> bool:
        return not line.startswith('#jp-')
