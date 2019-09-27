# Stubs for maxminddb.extension (Python 3)

from typing import Any, Mapping, Sequence

from maxminddb.errors import InvalidDatabaseError as InvalidDatabaseError

class Reader:
    closed: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def close(self, *args: Any, **kwargs: Any) -> Any: ...
    def get(self, *args: Any, **kwargs: Any) -> Any: ...
    def metadata(self, *args: Any, **kwargs: Any) -> Any: ...
    def __enter__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __exit__(self, *args: Any, **kwargs: Any) -> Any: ...

class extension:
    @property
    def node_count(self) -> int: ...
    @property
    def record_size(self) -> int: ...
    @property
    def ip_version(self) -> int: ...
    @property
    def database_type(self) -> str: ...
    @property
    def languages(self) -> Sequence[str]: ...
    @property
    def binary_format_major_version(self) -> int: ...
    @property
    def binary_format_minor_version(self) -> int: ...
    @property
    def build_epoch(self) -> int: ...
    @property
    def description(self) -> Mapping[str, str]: ...
    def __init__(self, **kwargs: Any) -> None: ...