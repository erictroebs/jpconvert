from ..operations import FilterLine


class RemoveMacrosFromCode(FilterLine):
    def filter_line(self, line: str) -> bool:
        return not line.startswith(('#jp-', '--jp-'))
