from argparse import ArgumentParser

from . import main

# parse command line arguments
parser = ArgumentParser()

parser.add_argument('input', help='notebook file (.ipynb) or - (stdin)')
parser.add_argument('--practice', '-p', action='store_true', default=False, help='keep practice (default)')
parser.add_argument('--solution', '-s', action='store_true', default=False, help='keep solution')
parser.add_argument('--teaching', '-t', action='store_true', default=False, help='keep teaching')
parser.add_argument('--allow-skip', action='store_true', default=False, help='do not remove cells without any macros')
parser.add_argument('--remove-empty', action='store_true', default=False, help='remove empty cells')
parser.add_argument('output', help='output file (.ipynb) or - (stdout, default)', nargs='?', default='-')

args = parser.parse_args()

# call main function
main(args.input, args.output,
     args.practice, args.solution, args.teaching,
     args.allow_skip, args.remove_empty)
