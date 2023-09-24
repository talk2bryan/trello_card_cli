# import the requests module
import os
from unittest.mock import Mock, patch

import pytest
import requests

from trello_card_cli.webservice import (
    create_trello_card,
    handle_http_error,
    send_request,
)


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    with patch.dict(
        os.environ, TRELLO_API_KEY="my_key", TRELLO_API_TOKEN="my_token", clear=True
    ):
        yield


def test_handle_http_error_401():
    """Test handle_http_error() with 401."""
    error = requests.exceptions.HTTPError(
        response=Mock(status_code=401), request=Mock()
    )

    with pytest.raises(ValueError, match="Invalid API key/token."):
        handle_http_error(error)


def test_handle_http_error_404():
    """Test handle_http_error() with 404."""
    error = requests.exceptions.HTTPError(
        response=Mock(status_code=404), request=Mock()
    )

    with pytest.raises(ValueError, match="Resource not found."):
        handle_http_error(error)


def test_send_request_200():
    """Test send_request() with 200."""
    with patch("requests.request") as mock_request:
        mock_request.return_value = Mock(
            status_code=200, json=Mock(return_value={"id": "test"})
        )
        response = send_request(path="/test", method="POST", params={"test": "test"})
        assert response == {"id": "test"}
        mock_request.assert_called_once_with(
            "POST",
            "https://api.trello.com/1/test",
            headers={"Accept": "application/json"},
            params={"test": "test"},
        )


def test_create_trello_card_one_label():
    """Test create_trello_card()."""
    with patch("trello_card_cli.webservice.send_request") as mock_send_request:
        mock_send_request.return_value = {"id": "test"}
        response = create_trello_card(
            list_id="test", labels=["test"], comment="test", name="test"
        )
        assert response == "test"
        mock_send_request.assert_called_once_with(
            path="/cards",
            method="POST",
            params={
                "idList": "test",
                "idLabels": "test",
                "desc": "test",
                "name": "test",
                "key": os.environ.get("TRELLO_API_KEY"),
                "token": os.environ.get("TRELLO_API_TOKEN"),
            },
        )


def test_create_trello_card_multiple_labels():
    """Test create_trello_card()."""
    with patch("trello_card_cli.webservice.send_request") as mock_send_request:
        mock_send_request.return_value = {"id": "test"}
        response = create_trello_card(
            list_id="test", labels=["test", "test2"], comment="test", name="test"
        )
        assert response == "test"
        mock_send_request.assert_called_once_with(
            path="/cards",
            method="POST",
            params={
                "idList": "test",
                "idLabels": "test,test2",
                "desc": "test",
                "name": "test",
                "key": os.environ.get("TRELLO_API_KEY"),
                "token": os.environ.get("TRELLO_API_TOKEN"),
            },
        )
