import argparse

from trello_card_cli.webservice import create_trello_card


def init_parser() -> argparse.ArgumentParser:
    """Initialize the parser for the CLI."""

    parser = argparse.ArgumentParser(
        prog="trello_card_cli",
        description="Trello Card CLI",
        usage="""trello_card_cli COMMAND [ARGS]...
        \n\nUse trello_card_cli COMMAND -h for more information about a command.""",
        epilog="%(prog)s was created by Bryan Wodi",
    )

    # Subparser for commands.
    subparser = parser.add_subparsers(title="Commands", dest="command", required=True)
    # add subparser. The only command we have right now.
    add_subparser = subparser.add_parser(
        "add", help="Add a card to a Trello list/column"
    )
    add_subparser.add_argument(
        "-n", "--name", help="Name of card to add. Required.", required=True
    )
    add_subparser.add_argument(
        "-c",
        "--comment",
        help="Comment (description) for card. Required",
        required=True,
    )
    add_subparser.add_argument(
        "--labels",
        help="Labels for a card, separated by space. Required",
        nargs="*",
        required=True,
    )
    add_subparser.add_argument(
        "-l",
        "--list_id",
        help="""List (column) ID to add card to. Optional. If not provided,
        will use the TRELLO_LIST_ID environment variable.""",
    )

    return parser


def parse_args(args: list) -> argparse.Namespace:
    """Parse the arguments from the CLI.

    Args:
        args (list): The arguments from the CLI.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = init_parser()
    return parser.parse_args(args)


def process_args(args: argparse.Namespace) -> None:
    """Process the arguments from the CLI.

    Args:
        args (argparse.Namespace): The arguments from the CLI.

    Raises:
        NotImplementedError: If the command is not implemented.
    """
    try:
        if args.command == "add":
            print("Adding card...")

            result = create_trello_card(
                list_id=args.list_id,
                labels=args.labels,
                comment=args.comment,
                name=args.name,
            )
            print(result)
        else:
            # Should only happen if we add a new command and forget to handle it here.
            raise NotImplementedError(f"The {args.command} command is not implemented.")
    except NotImplementedError as error:
        print(f"Error: {error}")
        exit(1)
