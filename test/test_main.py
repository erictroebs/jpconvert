from jpconvert import main


def test_practice():
    result = main('test/Untitled.ipynb', True, True, False, False, False, False)
    cells = result['cells']

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
    assert cell['source'] == ["a = 'practice'"]
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' not in cell['metadata'] or cell['metadata']['editable']

    # 3
    cell = cells[3]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ['b = a']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

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
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 8
    cell = cells[8]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Und eine leere Zelle zum Schluss:']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 9
    cell = cells[9]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == []
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']


def test_solution():
    result = main('test/Untitled.ipynb', True, False, True, False, False, False)
    cells = result['cells']

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
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

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
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 8
    cell = cells[8]
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Und eine leere Zelle zum Schluss:']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 9
    cell = cells[9]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == []
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']


def test_teaching():
    result = main('test/Untitled.ipynb', True, False, False, True, False, False)
    cells = result['cells']

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
    assert cell['cell_type'] == 'markdown'
    assert cell['source'] == ['Und eine leere Zelle zum Schluss:']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']

    # 7
    cell = cells[7]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == []
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']


def test_allow_skip():
    result = main('test/Untitled.ipynb', True, True, False, False, True, False)
    cells = result['cells']

    # len
    assert len(cells) == 11

    # 8
    cell = cells[8]
    assert cell['cell_type'] == 'code'
    assert cell['source'] == ['e = a']
    assert 'deletable' in cell['metadata'] and not cell['metadata']['deletable']
    assert 'editable' in cell['metadata'] and not cell['metadata']['editable']


def test_remove_empty():
    result = main('test/Untitled.ipynb', True, True, False, False, False, True)
    cells = result['cells']

    # len
    assert len(cells) == 8

    # check for empty cells
    for cell in cells:
        assert len(cell['source']) > 0
