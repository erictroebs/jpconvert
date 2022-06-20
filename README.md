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
python -m jpconvert <input> [<options>] [<output>]
```

If no output file is specified, `stdout` is used instead.

#### Macros and Options
Multiple macros can be used per cell. Only code cells with the macro matching the output options are kept. Macros themselves are removed from the code cells.

| macro          | option              |
| -------------- | ------------------- |
| `#jp-practice` | `--practice` / `-p` |
| `#jp-teaching` | `--teaching` / `-t` |
| `#jp-solution` | `--solution` / `-s` |

One may decide what happens to code cells without any macros. By default they are removed if `--allow-skip` is not used.


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
