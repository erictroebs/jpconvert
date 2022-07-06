from ..operations import MapLine


class StripLines(MapLine):
    def map_line(self, line: str) -> str:
        if line.endswith('\n'):
            return line.rstrip() + '\n'
        else:
            return line.rstrip()
