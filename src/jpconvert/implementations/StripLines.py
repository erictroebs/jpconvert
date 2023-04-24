from ..operations import MapLine


class StripLines(MapLine):
    def map_line(self, line: str) -> str:
        return line.rstrip()
