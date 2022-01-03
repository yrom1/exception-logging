# exception-logging-decorator
The following function:
```py
from typing import NoReturn

from exception_logger.main import exception_logger

log = exception_logger("./log.log", "US/Eastern")


@log
def no_return() -> NoReturn:
    """Test function."""
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")


if __name__ == "__main__":
    try:
        no_return()
    except:
        pass
```
Logs the following exception in `log.log`.
```
ERROR:root:no_return
  raised Exception: DO NOT PASS GO DO NOT COLLECT $200.
    called with args = (), kwargs = {}
    at 2022-01-02 22:46:10.702689-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/exception_logger/main.py", line 65, in wrapper
    output = function(*args, **kwargs)
  File "/home/ryan/exception-logging-decorator/test.py", line 11, in no_return
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")
Exception: DO NOT PASS GO DO NOT COLLECT $200.
```
