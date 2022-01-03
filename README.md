# exception-logging-decorator
The following function:
```py
@log
def no_return() -> NoReturn:
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")
```
Logs the following exception in `log.log`.
```
ERROR:root:no_return
  raised ValueError: DO NOT PASS GO DO NOT COLLECT $200.
    called with "args = (), kwargs = {}"
    at "2022-01-02 21:33:23.311281-05:00"
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/exception_logger/main.py", line 41, in wrapper
    output = function(*args, **kwargs)
  File "/home/ryan/exception-logging-decorator/test.py", line 11, in no_return
    raise ValueError("DO NOT PASS GO DO NOT COLLECT $200.")
ValueError: DO NOT PASS GO DO NOT COLLECT $200.

```
