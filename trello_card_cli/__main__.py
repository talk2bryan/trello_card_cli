"""Main entry point for the Trello Card CLI."""

import sys

from trello_card_cli.cli import parse_args, process_args

args = parse_args(sys.argv[1:])
process_args(args=args)
