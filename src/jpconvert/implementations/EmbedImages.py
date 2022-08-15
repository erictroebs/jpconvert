import json
from typing import Dict
from uuid import uuid4

from ..operations import MapCell
from base64 import b64encode
import requests
import os
import re
from typing import List, Tuple
import magic
import io


class EmbedImages(MapCell):
    FILE_EXTENSIONS = {
        'image/jpeg': 'jpg',
        'image/png': 'png'
    }

    def __init__(self):
        self._counter: int = 0

    @property
    def _new_identifier(self) -> str:
        self._counter += 1
        return str(self._counter)

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

                # store in attachments
                if path not in attachments:
                    # download image if http(s) resource
                    if path.startswith('http://') or path.startswith('https://'):
                        data = requests.get(path).content

                    # load image from disk
                    else:
                        with open(path, 'rb') as file:
                            data = file.read()

                    # store in attachments
                    mime_type = magic.from_buffer(data, mime=True)

                    file_ext = EmbedImages.FILE_EXTENSIONS[mime_type]
                    unique_name = f'{self._new_identifier}.{file_ext}'

                    if 'attachments' not in cell:
                        cell['attachments'] = {}

                    cell['attachments'][unique_name] = {
                        mime_type: b64encode(data).decode('ascii')
                    }

                    attachments[path] = unique_name

                # replace text
                start, end = match.span()
                start, end = cell['source'][i][:start], cell['source'][i][end:]
                replacement = f'![{description}](attachment:{attachments[path]})'

                cell['source'][i] = f'{start}{replacement}{end}'

        return cell
