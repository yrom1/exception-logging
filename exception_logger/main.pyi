from mypy_extensions import KwArg, VarArg
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[[VarArg(Any), KwArg(Any)], Any])

def exception_logger(filepath: str, timezone: str = ...) -> Callable[[F], F]: ...
