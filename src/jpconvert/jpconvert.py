import json
import sys
from typing import Callable, Any, Union, Optional


# util
def wrap(fun: Callable[[Any, ...], Any], *args):
    def wrapper(param: Any):
        return fun(param, *args)

    return wrapper


# functions
def filter_fun(cell: dict,
               practice: bool, solution: bool, teaching: bool,
               allow_skip: bool, remove_empty: bool) -> bool:
    if 'source' not in cell:
        return False
    if len(cell['source']) == 0:
        return not remove_empty
    if cell['cell_type'] != 'code':
        return True

    ml = min(3, len(cell['source']))

    if allow_skip and not any([
        any([cell['source'][i].strip().lower() == '#jp-practice' for i in range(ml)]),
        any([cell['source'][i].strip().lower() == '#jp-solution' for i in range(ml)]),
        any([cell['source'][i].strip().lower() == '#jp-teaching' for i in range(ml)])
    ]):
        return True

    return any([
        any([cell['source'][i].strip().lower() == '#jp-practice' for i in range(ml)]) and practice,
        any([cell['source'][i].strip().lower() == '#jp-solution' for i in range(ml)]) and solution,
        any([cell['source'][i].strip().lower() == '#jp-teaching' for i in range(ml)]) and teaching
    ])


def map_fun(cell: dict) -> dict:
    # change metadata
    cell['metadata']['deletable'] = False

    if 'pycharm' in cell['metadata']:
        del cell['metadata']['pycharm']

    # set other cells to readonly
    if cell['cell_type'] != 'code':
        cell['metadata']['editable'] = False

    # remove macros
    elif 'source' in cell:
        editable = 0

        while len(cell['source']) > 0:
            if cell['source'][0].strip().lower() == '#jp-practice':
                del cell['source'][0]
                editable += 1
            elif cell['source'][0].strip().lower() == '#jp-solution':
                del cell['source'][0]
                editable -= 1
            elif cell['source'][0].strip().lower() == '#jp-teaching':
                del cell['source'][0]
                editable -= 1
            else:
                break

        cell['metadata']['editable'] = (editable > 0)

    return cell


# main script
def main(input_file: str, output_file: Union[str, bool],
         practice: bool, solution: bool, teaching: bool,
         allow_skip: bool, remove_empty: bool) -> Optional[dict]:
    if not practice and not solution and not teaching:
        practice = True
    if practice:
        solution = False
        teaching = False
    if solution:
        practice = False
        teaching = False
    if teaching:
        practice = False
        solution = False

    # read input
    if input_file == '-':
        data = json.load(sys.stdin)
    else:
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # convert cells
    data['cells'] = list(map(
        map_fun,
        filter(
            wrap(filter_fun, practice, solution, teaching, allow_skip, remove_empty),
            data['cells']
        )
    ))

    # remove tag bar
    if 'celltoolbar' in data['metadata']:
        del data['metadata']['celltoolbar']

    # write to stdout
    if isinstance(output_file, bool):
        return data

    if output_file == '-':
        print(json.dumps(data, indent=4))
    else:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
