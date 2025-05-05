from unittest.mock import MagicMock

import pytest

from pywebclient.client import ClientConfig


@pytest.fixture
def mock_client_config() -> ClientConfig:
    mock = MagicMock(spec=ClientConfig)
    mock.api_version = "v1"
    return mock


class TestClientConfig:

    def test_client_config(self, mock_client_config):

        assert mock_client_config is not None
        assert isinstance(mock_client_config, ClientConfig)