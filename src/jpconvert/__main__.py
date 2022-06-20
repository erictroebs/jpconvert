import json
import sys
from argparse import ArgumentParser

# configure argument parser
parser = ArgumentParser()

parser.add_argument('input', help='notebook file (.ipynb) or - (stdin)')
parser.add_argument('--practice', '-p', action='store_true', default=False, help='keep practice (default)')
parser.add_argument('--solution', '-s', action='store_true', default=False, help='keep solution')
parser.add_argument('--teaching', '-t', action='store_true', default=False, help='keep teaching')
parser.add_argument('--allow-skip', action='store_true', default=False, help='do not remove cells without any macros')
parser.add_argument('output', help='output file (.ipynb) or - (stdout, default)', nargs='?', default='-')

args = parser.parse_args()

if not args.practice and not args.solution and not args.teaching:
    args.practice = True
if args.practice:
    args.solution = False
    args.teaching = False
if args.solution:
    args.practice = False
    args.teaching = False
if args.teaching:
    args.practice = False
    args.solution = False


# functions
def filter_fun(cell: dict) -> bool:
    if cell['cell_type'] != 'code':
        return True
    if 'source' not in cell or len(cell['source']) == 0:
        return True

    ml = min(3, len(cell['source']))

    if args.allow_skip and not any([
        any([cell['source'][i].strip().lower() == '#jp-practice' for i in range(ml)]),
        any([cell['source'][i].strip().lower() == '#jp-solution' for i in range(ml)]),
        any([cell['source'][i].strip().lower() == '#jp-teaching' for i in range(ml)])
    ]):
        return True

    return any([
        any([cell['source'][i].strip().lower() == '#jp-practice' for i in range(ml)]) and args.practice,
        any([cell['source'][i].strip().lower() == '#jp-solution' for i in range(ml)]) and args.solution,
        any([cell['source'][i].strip().lower() == '#jp-teaching' for i in range(ml)]) and args.teaching
    ])


def map_fun(cell: dict) -> dict:
    # change metadata
    cell['metadata']['deletable'] = False

    if 'pycharm' in cell['metadata']:
        del cell['metadata']['pycharm']

    # remove flags
    if cell['cell_type'] == 'code' and 'source' in cell:
        editable = False

        while len(cell['source']) > 0:
            if cell['source'][0].strip().lower() == '#jp-practice':
                del cell['source'][0]
                editable = True
            elif cell['source'][0].strip().lower() == '#jp-solution':
                del cell['source'][0]
            elif cell['source'][0].strip().lower() == '#jp-teaching':
                del cell['source'][0]
            else:
                break

        if not editable:
            cell['metadata']['editable'] = False

    return cell


# main script
def main():
    # read input
    if args.input == '-':
        data = json.load(sys.stdin)
    else:
        with open(args.input, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # convert cells
    data['cells'] = list(map(map_fun, filter(filter_fun, data['cells'])))

    # remove tag bar
    if 'celltoolbar' in data['metadata']:
        del data['metadata']['celltoolbar']

    # write to stdout
    if args.output == '-':
        print(json.dumps(data, indent=4))
    else:
        with open(args.output, 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == '__main__':
    main()
