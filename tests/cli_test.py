from trello_card_cli.cli import init_parser, process_args


def test_init_parser():
    """Test init_parser()."""
    usage = """trello_card_cli COMMAND [ARGS]...
        \n\nUse trello_card_cli COMMAND -h for more information about a command."""
    parser = init_parser()
    assert parser.prog == "trello_card_cli"
    assert parser.description == "Trello Card CLI"
    assert parser.usage == usage
    assert parser.epilog == "%(prog)s was created by Bryan Wodi"


def test_parse_args():
    """Test parse_args()."""
    parser = init_parser()
    args = parser.parse_args(
        args=["add", "-n", "test", "-c", "test", "--labels", "test"]
    )
    assert args.command == "add"
    assert args.name == "test"
    assert args.comment == "test"
    assert args.labels == ["test"]
    assert args.list_id is None


def test_process_args(capsys):
    """Test process_args()."""
    parser = init_parser()
    args = parser.parse_args(
        args=["add", "-n", "test", "-c", "test", "--labels", "test"]
    )
    process_args(args=args)
    captured = capsys.readouterr()
    assert captured.out is not None
    assert "Adding card" in captured.out
