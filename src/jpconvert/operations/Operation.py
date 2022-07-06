from typing import Dict, Optional


class Operation:
    def __call__(self, cell: Dict) -> Optional[Dict]:
        raise NotImplementedError

    def exit(self):
        pass
