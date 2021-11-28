# exception-logging-decorator
The following function:
```py
@log
def no_return() -> NoReturn:
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")
```
Logs the following exception in `log.log`.
```
ERROR:root:Exception raised in function "no_return"
 called with args "" at "2021-11-28 13:49:49.891050-05:00".
 exception: "DO NOT PASS GO DO NOT COLLECT $200."
Traceback (most recent call last):
  File "main.py", line 48, in wrapper
    output = function(*args, **kwargs)
  File "main.py", line 64, in no_return
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")
Exception: DO NOT PASS GO DO NOT COLLECT $200.

```
