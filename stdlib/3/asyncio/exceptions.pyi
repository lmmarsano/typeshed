import sys
from typing import List, Optional

if sys.version_info >= (3, 8):
    class CancelledError(BaseException): ...
    class TimeoutError(Exception): ...
    class InvalidStateError(Exception): ...
    class SendfileNotAvailableError(RuntimeError): ...
    class IncompleteReadError(EOFError):
        expected: Optional[int]
        partial: bytes
        def __init__(self, partial: bytes, expected: Optional[int]) -> None: ...
    class LimitOverrunError(Exception):
        consumed: int
        def __init__(self, message: str, consumed: int) -> None: ...

    __all__: List[str]