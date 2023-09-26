# Trello Card API

This is a CLI program with Python that adds cards to a trello.com board.

Interaction with the Trello API was designed and implementated based on [the
official documentation](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post).

### Technologies
- Python version 3.10
- [Pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)

### Project organization
```
.
├── .env
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── pyproject.toml
├── README.md
├── setup.cfg
├── tests
│   ├── cli_test.py
│   ├── __init__.py
│   └── webservice_test.py
└── trello_card_cli
    ├── cli.py
    ├── __init__.py
    ├── __main__.py
    └── webservice.py
```
`.env` - Contains the application secrets/environment variables.
`.pre-commit-config.yaml` - Contains the configurations for pre-commit.
`.python-version` - Contains the Python version.
`Pipfile*` - The pipenv equivalent of requirements.txt for package and virtual environment management.
`pyproject.toml` - A TOML file that specifies the project's build system and other configurations.
`setup.cfg` - An empty placeholder file necessary for pipenv install to succeed.
`tests/` - Contains the test cases for the application.
`trello_card_cli/`: Contains the main source code for the CLI application. `__main__.py` is the entry point for the application.

### First time set up?
- Install pipenv by following the URL above
- The following must be run from this directory
`cat .python-version | xargs pipenv --python`
`pipenv install --dev`
`pipenv run pre-commit install`
- Modify the environment variables in the `trello_card_cli/.env` file
- Run the application:
`pipenv run python -m  trello_card_cli add -c COMMENT --labels label1 label2 -n NAME [-l LIST_ID]`


### Testing
`pipenv run pytest`

### License Information
You may view this repository, and talk about it. See LICENSE for more.

### Status
The application is currently in a functional state. Its only capability is adding trello cards to a pre-existing board, where the ID of the column of the board is provided by the user.
