"""Base API client class for assyncronous HTTP requests."""

import logging
from dataclasses import dataclass, field
from typing import Annotated, Any, Callable, Dict, List, Optional, Tuple

from httpx import Response

logger = logging.getLogger(__name__)

ResponseExtractorType = Callable[[Response], Tuple[Optional[str], int]]
PageProcessorType = Callable[[Dict[str, Any]], List[Dict[str, Any]]]


@dataclass
class ClientConfig:
    # API Configuration
    api_version: str = "v1"
    accept_header: str = "application/json"
    base_url: Annotated[str, field(default="")] = ""
    verify_ssl: bool = True

    # Pagination Configuration
    page_size: int = 100
    first_page: int = 1
    max_pages: int = 100

    # Rate Limiting and Retry Configuration
    max_retries: int = 3
    base_retry_delay: float = 1.0
    max_retry_delay: float = 10.0
    jitter_factor: float = 0.25
    max_concurrent_rrequests: int = 5

    @classmethod
    def default(cls) -> "ClientConfig":
        """Returns the default configuration."""

        return cls()
