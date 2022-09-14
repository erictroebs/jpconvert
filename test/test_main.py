import json
import os

from jpconvert import build_pipeline, Pipeline, EmbedImages


def run(path: str, pipeline: Pipeline):
    if os.path.exists('test/'):
        os.chdir('test/')

    with open(path, 'r') as file:
        input_data = json.load(file)

    output = pipeline.run(input_data)

    with open('output.ipynb', 'w') as file:
        json.dump(output, file)

    return output['cells']


def test_practice():
    cells = run('ExampleCode.ipynb',
                build_pipeline(True, False, False, False, False, False, False, False))

    # len
    assert len(cells) == 13

    # 0
    cell = cells[0]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['# Überschrift']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 1
    cell = cells[1]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Unnötig langer Text...']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 2
    cell = cells[2]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ["a = 'practice'"]
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' not in cell['metadata'] or cell['metadata']['editable']

    # 3
    cell = cells[3]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ['b = a']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' not in cell['metadata'] or cell['metadata']['editable']

    # 4
    cell = cells[4]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Eine leere Zelle zwischendurch:']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 5
    cell = cells[5]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == []
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 6
    cell = cells[6]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Zwischentext...']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 7
    cell = cells[7]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ['d = a']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' not in cell['metadata'] or cell['metadata']['editable']

    # 8
    cell = cells[8]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ['e = a']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 9
    cell = cells[9]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Und eine leere Zelle zum Schluss:']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 10
    cell = cells[10]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == []
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' not in cell['metadata'] or cell['metadata']['editable']

    # 11
    cell = cells[11]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ["y = 'readonly'"]
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 12
    cell = cells[12]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ["z = 'readonly'"]
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']


def test_solution():
    cells = run('ExampleCode.ipynb',
                build_pipeline(False, True, False, False, False, False, False, False))

    # len
    assert len(cells) == 10

    # 0
    cell = cells[0]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['# Überschrift']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 1
    cell = cells[1]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Unnötig langer Text...']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 2
    cell = cells[2]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ["a = 'solution'"]
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 3
    cell = cells[3]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ['b = a']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' not in cell['metadata'] or cell['metadata']['editable']

    # 4
    cell = cells[4]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Eine leere Zelle zwischendurch:']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 5
    cell = cells[5]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == []
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 6
    cell = cells[6]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Zwischentext...']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 7
    cell = cells[7]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ['d = a']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' not in cell['metadata'] or cell['metadata']['editable']

    # 8
    cell = cells[8]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ['e = a']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 9
    cell = cells[9]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Und eine leere Zelle zum Schluss:']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']


def test_teaching():
    cells = run('ExampleCode.ipynb',
                build_pipeline(False, False, True, False, False, False, False, False))

    # len
    assert len(cells) == 8

    # 0
    cell = cells[0]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['# Überschrift']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 1
    cell = cells[1]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Unnötig langer Text...']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 2
    cell = cells[2]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Eine leere Zelle zwischendurch:']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 3
    cell = cells[3]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == []
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 4
    cell = cells[4]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Zwischentext...']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 5
    cell = cells[5]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ['c = a']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 6
    cell = cells[6]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ['e = a']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 7
    cell = cells[7]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Und eine leere Zelle zum Schluss:']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']


def test_remove_without_macros():
    cells = run('ExampleCode.ipynb',
                build_pipeline(True, False, False, True, False, False, False, False))

    # len
    assert len(cells) == 11

    # 5
    cell = cells[5]
    assert cell['source'] != []

    # 8
    cell = cells[8]
    assert cell['source'] != ['e = a']


def test_remove_empty():
    cells = run('ExampleCode.ipynb',
                build_pipeline(True, False, False, False, True, False, False, False))

    # len
    assert len(cells) == 11

    # check for empty cells
    for cell in cells:
        assert len(cell['source']) > 0


def test_toc():
    cells = run('ExampleToc.ipynb',
                build_pipeline(True, False, False, True, True, False, False, False))

    # 1
    assert cells[1]['cell_type'] == 'markdown'
    assert cells[1]['source'] == ['# Inhaltsverzeichnis\n',
                                  '- [TOC Test](#TOC-Test)\n',
                                  '  - [Code](#Code)\n',
                                  '  - [Text](#Text)\n',
                                  '  - [Mix](#Mix)\n',
                                  '    - [another heading](#another-heading)\n',
                                  '      - [even smaller heading](#even-smaller-heading)']

    # 3
    assert cells[3]['cell_type'] == 'markdown'
    assert cells[3]['source'] == ['## Inhaltsverzeichnis\n',
                                  '- [Code](#Code)\n',
                                  '- [Text](#Text)\n',
                                  '- [Mix](#Mix)\n',
                                  '  - [another heading](#another-heading)\n',
                                  '    - [even smaller heading](#even-smaller-heading)']

    # 4
    assert cells[4]['cell_type'] == 'markdown'
    assert cells[4]['source'] == ['# Inhaltsverzeichnis\n',
                                  '- [TOC Test](#TOC-Test)\n',
                                  '  - [Code](#Code)\n',
                                  '  - [Text](#Text)\n',
                                  '  - [Mix](#Mix)']

    # 5
    assert cells[5]['cell_type'] == 'markdown'
    assert cells[5]['source'] == ['# Inhaltsverzeichnis\n',
                                  '- [TOC Test](#TOC-Test)\n',
                                  '  - [Code](#Code)\n',
                                  '  - [Text](#Text)\n',
                                  '  - [Mix](#Mix)']


def test_strip_lines():
    cells = run('ExampleLines.ipynb',
                build_pipeline(True, False, False, False, False, True, False, False))

    # len
    assert len(cells) == 12

    # 1
    assert cells[1]['source'] == ['this = 1\n',
                                  "my = 'code'"]

    # 3
    assert cells[3]['source'] == ['this = 1\n']

    # 5
    assert cells[5]['source'] == ['\n']

    # 7
    assert cells[7]['source'] == ['']

    # 8
    assert cells[8]['source'] == ['']

    # 10
    assert cells[10]['source'] == ['\n', '']

    # 11
    assert cells[11]['source'] == ['\n', '']


def test_trailing_lines():
    cells = run('ExampleLines.ipynb',
                build_pipeline(True, False, False, False, False, True, True, False))

    # len
    assert len(cells) == 12

    # 1
    assert cells[1]['source'] == ['this = 1\n',
                                  "my = 'code'"]

    # 3
    assert cells[3]['source'] == ['this = 1']

    # 5
    assert cells[5]['source'] == []

    # 7
    assert cells[7]['source'] == []

    # 8
    assert cells[8]['source'] == []

    # 10
    assert cells[10]['source'] == []

    # 11
    assert cells[11]['source'] == []


def test_embed_image():
    cells = run('ExampleImages.ipynb',
                build_pipeline(True, False, False, False, False, False, False, True))

    # 0
    assert 'attachments' in cells[0]
    assert cells[0]['source'] == [
        "# ExampleImages\n",
        "![png description](attachment:1.png)"
    ]

    # 1
    assert 'attachments' in cells[1]
    assert cells[1]['source'] == [
        "Test\n",
        "![jpeg description](attachment:2.jpg)"
    ]

    # 2
    assert 'attachments' in cells[2]
    assert cells[2]['source'] == [
        "![url description](attachment:3.jpg)"
    ]

    # 3
    assert 'attachments' in cells[3]
    assert cells[3]['source'] == [
        "Inline test with ![image](attachment:4.png) from the first cell."
    ]

    # 4
    assert 'attachments' in cells[4]
    assert cells[4]['source'] == [
        "Inline test with![image](attachment:5.png)missing spaces."
    ]

    # 5
    assert 'attachments' in cells[5]
    assert cells[5]['source'] == [
        "Two images in the same cell\n",
        "![jpeg description](attachment:6.jpg)\n",
        "![jpeg description](attachment:7.png)"
    ]

    # 6
    assert 'attachments' in cells[6]
    assert cells[6]['source'] == [
        "Same images in the same cell\n",
        "![jpeg description](attachment:8.jpg)\n",
        "![jpeg description](attachment:8.jpg)"
    ]

    # 7
    assert 'attachments' in cells[7]
    assert cells[7]['source'] == [
        "Two images in one line\n",
        "text ![jpeg description](attachment:10.jpg) text ![jpeg description](attachment:9.png) text"
    ]

    # 8
    png_b64, *_ = EmbedImages.base64encode('example.png')
    assert cells[8]['source'] == [
        'Sample image included via html tag\n',
        f'<img src="data:image/png;base64,{png_b64}">'
    ]

    # 9
    jpg_b64, *_ = EmbedImages.base64encode('https://picsum.photos/id/1024/300/200')
    assert cells[9]['source'] == [
        'Remote image included via html tag with alt attribute\n',
        f'<img alt="birb" src="data:image/jpeg;base64,{jpg_b64}">'
    ]

    # 10
    png_b64, *_ = EmbedImages.base64encode('example.png')
    assert cells[10]['source'] == [
        'Two img tags in one line\n',
        f'<img src="data:image/png;base64,{png_b64}"><img src="data:image/png;base64,{png_b64}">'
    ]

    # 11
    assert cells[11]['source'] == [
        'An already attached image:\n',
        '![example.png](attachment:example.png)'
    ]

    # 12
    assert 'attachments' in cells[12]
    assert cells[12]['source'] == [
        'svg:\n',
        '![example.svg](attachment:11.svg)'
    ]

    # 13
    svg_b64, *_ = EmbedImages.base64encode('example.svg')
    assert cells[13]['source'] == [
        'svg via img tag:\n',
        f'<img src="data:image/svg+xml;base64,{svg_b64}">'
    ]

    # 14
    assert cells[14]['source'] == [
        'An already attached svg:\n',
        '![example.svg](attachment:example.svg)'
    ]

    # 15
    svg_b64, *_ = EmbedImages.base64encode('example_gray.png')
    assert cells[15]['source'] == [
        'images included as base64 string:\n',
        f'![test](data:image/png;base64,{svg_b64})\n',
        f'<img src="data:image/png;base64,{svg_b64}">'
    ]
