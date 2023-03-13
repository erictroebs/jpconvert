import re
from base64 import b64encode
from typing import Dict, Tuple
from typing import List

import magic
import requests

from ..operations import MapCell


class EmbedImages(MapCell):
    FILE_EXTENSIONS = {
        'image/jpeg': 'jpg',
        'image/png': 'png',
        'image/svg+xml': 'svg'
    }

    def __init__(self):
        self._counter: int = 0

    @property
    def _new_identifier(self) -> str:
        self._counter += 1
        return str(self._counter)

    @staticmethod
    def base64encode(path: str) -> Tuple[str, str, str]:
        # download image if http(s) resource
        if path.startswith('http://') or path.startswith('https://'):
            data = requests.get(path).content

        # load image from disk
        else:
            with open(path, 'rb') as file:
                data = file.read()

        # get mime type and file extension
        mime_type = magic.from_buffer(data, mime=True)
        file_ext = EmbedImages.FILE_EXTENSIONS[mime_type]

        # base64 encode
        base64_data = b64encode(data).decode('ascii')

        # return tuple
        return base64_data, mime_type, file_ext

    def map_cell(self, cell: Dict):
        # skip cells not containing markdown
        if cell['cell_type'] != 'markdown':
            return cell

        # find images in markdown
        attachments: Dict[str, str] = {}

        for i in range(len(cell['source'])):
            matches: List[re.Match] = list(re.finditer(r'!\[(.*?)\]\((.*?)\)', cell['source'][i]))
            matches.reverse()

            for match in matches:
                # extract description and path
                description, path = match.groups()

                # skip already attached images
                if path.startswith('attachment:') or path.startswith('data:'):
                    continue

                # store in attachments
                if path not in attachments:
                    base64_data, mime_type, file_ext = self.base64encode(path)
                    unique_name = f'{self._new_identifier}.{file_ext}'

                    if 'attachments' not in cell:
                        cell['attachments'] = {}

                    cell['attachments'][unique_name] = {
                        mime_type: base64_data
                    }

                    attachments[path] = unique_name

                # replace text
                start, end = match.span()
                start, end = cell['source'][i][:start], cell['source'][i][end:]
                replacement = f'![{description}](attachment:{attachments[path]})'

                cell['source'][i] = f'{start}{replacement}{end}'

        # find images in <img> tags
        for i in range(len(cell['source'])):
            if '<img' not in cell['source'][i]:
                continue

            matches: List[re.Match] = list(re.finditer(r'<img[^>]+src="(.*?)"[^>]*>', cell['source'][i]))
            matches.reverse()

            for match in matches:
                # extract source
                src = match.group(1)

                if src.startswith('data:'):
                    continue

                # base64 encode data
                base64_data, mime_type, _ = self.base64encode(src)

                # replace text
                start, end = match.span(1)
                start, end = cell['source'][i][:start], cell['source'][i][end:]
                replacement = f'data:{mime_type};base64,{base64_data}'

                cell['source'][i] = f'{start}{replacement}{end}'

        return cell
