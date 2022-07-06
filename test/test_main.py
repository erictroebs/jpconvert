import json

from jpconvert import build_pipeline, Pipeline


def run(path: str, pipeline: Pipeline):
    with open(path, 'r') as file:
        input_data = json.load(file)

    return pipeline.run(input_data)['cells']


def test_practice():
    cells = run('test/ExampleCode.ipynb',
                build_pipeline(True, False, False, False, False, False, False))

    # len
    assert len(cells) == 11

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


def test_solution():
    cells = run('test/ExampleCode.ipynb',
                build_pipeline(False, True, False, False, False, False, False))

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
    cells = run('test/ExampleCode.ipynb',
                build_pipeline(False, False, True, False, False, False, False))

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
    cells = run('test/ExampleCode.ipynb',
                build_pipeline(True, False, False, True, False, False, False))

    # len
    assert len(cells) == 9

    # 5
    cell = cells[5]
    assert cell['source'] != []

    # 8
    cell = cells[8]
    assert cell['source'] != ['e = a']


def test_remove_empty():
    cells = run('test/ExampleCode.ipynb',
                build_pipeline(True, False, False, False, True, False, False))

    # len
    assert len(cells) == 9

    # check for empty cells
    for cell in cells:
        assert len(cell['source']) > 0


def test_toc():
    cells = run('test/ExampleToc.ipynb',
                build_pipeline(True, False, False, True, True, False, False))

    # 1
    assert cells[1]['cell_type'] == 'markdown'
    assert cells[1]['source'] == ['- TOC Test\n',
                                  '  - Code\n',
                                  '  - Text\n',
                                  '  - Mix\n',
                                  '    - another heading\n',
                                  '      - even smaller heading\n']

    # 3
    assert cells[3]['cell_type'] == 'markdown'
    assert cells[3]['source'] == ['- Code\n',
                                  '- Text\n',
                                  '- Mix\n',
                                  '  - another heading\n',
                                  '    - even smaller heading\n']

    # 4
    assert cells[4]['cell_type'] == 'markdown'
    assert cells[4]['source'] == ['- TOC Test\n',
                                  '  - Code\n',
                                  '  - Text\n',
                                  '  - Mix\n']

    # 5
    assert cells[5]['cell_type'] == 'markdown'
    assert cells[5]['source'] == ['- TOC Test\n',
                                  '  - Code\n',
                                  '  - Text\n',
                                  '  - Mix\n']


def test_strip_lines():
    cells = run('test/ExampleLines.ipynb',
                build_pipeline(True, False, False, False, False, True, False))

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
    cells = run('test/ExampleLines.ipynb',
                build_pipeline(True, False, False, False, False, True, True))

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
