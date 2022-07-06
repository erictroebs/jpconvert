# JPConvert
JPConvert is a simple tool to split up Jupyter Notebooks based on macros and remove unnecessary metadata.


## Installation
JPConvert does not need any libraries. It is probably a good idea to use `nbstripout` with it though.

The preferred way to use JPConvert is in a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

Use pip to download and install JPConvert:
```bash
pip install jpconvert
```


## Usage
```bash
python -m jpconvert <input> [<output>] [<options>]
```

If no input file is specified, `stdin` is used instead. If no output file is specified, `stdout` is used instead.

#### Macros and Options
| option                    | description                                   |
|---------------------------|-----------------------------------------------|
| `--practice` / `-p`       | keep cells containing `#jp-practice`          |
| `--teaching` / `-t`       | keep cells containing `#jp-teaching`          |
| `--solution` / `-s`       | keep cells containing `#jp-solution`          |
| `--remove-without-macros` | remove cells that do not contain any macro    |
| `--keep-empty`            | do not remove empty cells                     |
 | `--no-strip-lines`        | do not remove space or tabs from line endings |
| `--keep-trailing`         | do not remove trailing lines                  |

Multiple macros can be used per cell. Only code cells with the macro matching the output options are kept. Macros themselves are removed from the code cells.

The special macro `#jp-toc` can be used to create a table of contents. Up to two conditionals can be added to control the table's depth.


## Example
Image two code cells inside your notebook:
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
