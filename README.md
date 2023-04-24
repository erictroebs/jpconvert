# JPConvert

JPConvert is a preprocessor for Jupyter Notebooks. It may be used to split up Jupyter Notebooks based on macros,
automatically set options, embed images and remove unnecessary metadata.

## Quick Start

Install JPConvert:

```bash
pip install jpconvert
```

Imagine two code cells inside your notebook:

```python
#jp-solution
a = a + 1
```

```python
#jp-practice
a = ...
```

If you call JPConvert with the `--practice` option, the first cell is removed and the second cell is kept:

```python
a = ...
```

If you call JPConvert with the `--solution` option, the first cell is kept and the second cell is removed:

```python
a = a + 1
```

## Setup

The preferred way to use JPConvert is in a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Use pip to download and install JPConvert. JPConvert requires `requests` and `python-magic` to embed images via HTTP.
Both packages are installed automatically by pip.

```bash
pip install jpconvert
```

Run JPConvert as a Python module:

```bash
python -m jpconvert <input> [<output>] [<options>]
```

## Usage Guide

### Macros and Output Types

JPConvert provides several macros to mark cells for a specific task. Only code cells with the macro matching the output
options are kept.

| cli option          | description                          |
|---------------------|--------------------------------------|
| `--practice` / `-p` | keep cells containing `#jp-practice` |
| `--teaching` / `-t` | keep cells containing `#jp-teaching` |
| `--solution` / `-s` | keep cells containing `#jp-solution` |

Multiple macros can be used per cell. Macros themselves are removed from the code cells.

Instead of `#` you can also use `--`. The macros without any prefix can also be added as tags to individual cells.

It is also possible to remove any cells without macros. Add `--remove-without-macros` to the command line parameters
to activate this behavior.

### Empty Cells, Empty Lines, Trailing Spaces

JPConvert automatically removes

1. trailing spaces from lines,
2. empty lines from the end of cells and
3. empty cells.

This behavior can be disabled using the command line parameters

1. `--no-strip-lines`,
2. `--keep-trailing` and
3. `--keep-empty`.

### Readonly and Undeletable

JPConvert automatically adds *readonly* and *undeletable* flags to any cells that do not contain `#jp-practice`. If you
want to protect the latter from writing as well, add `#jp-readonly` or use `#jp-practice-ro`. Users may undo these
changes, but at least they cannot accidentally delete or modify cells.

To disable this behavior, the command line parameters `--no-force-readonly` and `--no-set-undeletable` can be used.

### Table of Contents

A table of contents is automatically inserted into all cells that contain the macro `#jp-toc`. The entries are
automatically generated from headlines (lines starting with one or multiple `#`) in markdown cells. Each entry consists
of the title and a reference that leads directly to the anchor tag of the heading.

Up to two conditionals can be added to control the table's depth. It uses the level of the heading (number of `#`) for
filtering. The following example shows how to create a table of contents from level 2 to 5.

```python
#jp-toc>=2<6
```

### Embedding Images

Images can be embedded in markdown cells via the Jupyter user interface. JPConvert automatically embeds linked files
from both local disk and HTTP(S) sources, which simplifies notebook editing. Supported file types are `png`, `jpg` and
`svg`.

JPConvert also embeds files that are displayed using HTML tags. These provide the ability to scale graphics as desired,
while in markdown the size is determined only by the resolution.

Add the command line parameter `--no-embed-images` to disable this behavior.

### Stripping Output

`execution_count` is set to `None` and `output` is set to an empty array for each individual code cell. (Which is
basically the functionality of *nbstripout*.)

Add the command line parameter `--keep-output` to disable this behavior.
