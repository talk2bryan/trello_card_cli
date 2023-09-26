import os
from typing import Final

import requests


def handle_http_error(error: requests.exceptions.HTTPError) -> None:
    """Handle HTTP errors.

    Args:
        e (requests.exceptions.HTTPError): The HTTP error.
    """
    if error.response.status_code == 401:
        raise ValueError("Invalid API key/token.")
    if error.response.status_code == 404:
        raise ValueError("Resource not found.")

    raise IOError("Unknown HTTP error.")


def send_request(path: str, method: str, params: dict) -> dict:
    """Send a request to the Trello API.

    Args:
        path (str): The path to the endpoint.
        method (str): The HTTP method to use.
        params (dict): The parameters to send.
        params (int): The timeout in seconds. Defaults to 10.

    Returns:
        dict: The response as a dictionary.
    """
    TRELLO_API_URL: Final[str] = os.environ.get(
        "TRELLO_API_URL", "https://api.trello.com/1"
    )
    url = f"{TRELLO_API_URL}{path}"
    headers = {"Accept": "application/json"}

    if method != "POST":
        raise NotImplementedError("Only POST requests are supported.")

    try:
        response = requests.request(method, url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as error:
        handle_http_error(error)
        raise
    except Exception as error:
        raise IOError(f"Unknown error: {error}") from error


def create_trello_card(
    name: str,
    comment: str,
    labels: list[str],
    list_id: str | None = None,
) -> str:
    """Create a Trello card.

    Args:
        name (str): The name of the card.
        comment (str): The comment (description) to add to the card.
        labels (list[str]): The labels to add to the card.
        list_id (str, optional): The ID of the list/column to add the card to. Defaults to None.

    Returns:
        str: The ID of the created card.
    """
    list_id = list_id if list_id else os.environ.get("TRELLO_LIST_ID")
    path = "/cards"
    method = "POST"
    params = {
        "idList": list_id,
        "idLabels": ",".join(labels),
        "desc": comment,
        "name": name,
        "key": os.environ.get("TRELLO_API_KEY"),
        "token": os.environ.get("TRELLO_API_TOKEN"),
    }
    try:
        data = send_request(path=path, method=method, params=params)
        success_response = f"Created card with ID: {data['id']}"
        return success_response

    except (KeyError, ValueError, IOError) as error:
        return f"Could not create card: {error}"
