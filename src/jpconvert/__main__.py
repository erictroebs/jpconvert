import nbformat
import sys
from argparse import ArgumentParser
from nbformat import NotebookNode

from . import build_pipeline

# parse command line arguments
parser = ArgumentParser()

parser.add_argument('input',
                    help='notebook file (.ipynb) or - (stdin)')
parser.add_argument('--practice', '-p', action='store_true', default=False,
                    help='keep practice (default)')
parser.add_argument('--solution', '-s', action='store_true', default=False,
                    help='keep solution')
parser.add_argument('--teaching', '-t', action='store_true', default=False,
                    help='keep teaching')
parser.add_argument('--remove-without-macros', action='store_true', default=False,
                    help='remove code cells without macros')
parser.add_argument('--keep-empty', action='store_true', default=False,
                    help='keep empty cells')
parser.add_argument('--no-strip-lines', action='store_true', default=False,
                    help='do not strip lines')
parser.add_argument('--keep-trailing', action='store_true', default=False,
                    help='keep empty trailing lines')
parser.add_argument('--no-embed-images', action='store_true', default=False,
                    help='do not embed images in output file')
parser.add_argument('--no-force-readonly', action='store_true', default=False,
                    help='do not automatically set code cells to readonly')
parser.add_argument('--no-set-undeletable', action='store_true', default=False,
                    help='do not protect cells from deletion')
parser.add_argument('--keep-output', action='store_true', default=False,
                    help='do not delete output from cells')
parser.add_argument('output', nargs='?', default='-',
                    help='output file (.ipynb) or - (stdout, default)')

args = parser.parse_args()

# ensure exclusivity of some parameters
practice = args.practice
solution = args.solution
teaching = args.teaching

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
if args.input == '-':
    input_data: NotebookNode = nbformat.read(sys.stdin, nbformat.NO_CONVERT)
else:
    with open(args.input, 'r', encoding='utf-8') as file:
        input_data: NotebookNode = nbformat.read(file, nbformat.NO_CONVERT)

# run pipeline
pipeline = build_pipeline(practice, solution, teaching,
                          args.remove_without_macros, not args.keep_empty,
                          not args.no_strip_lines, not args.keep_trailing,
                          not args.no_embed_images,
                          not args.no_force_readonly, not args.no_set_undeletable,
                          not args.keep_output)
output_data = pipeline.run(input_data)

# write output
if args.output == '-':
    print(nbformat.writes(output_data, indent=4))
else:
    with open(args.output, 'w') as file:
        nbformat.write(output_data, file, indent=4)
