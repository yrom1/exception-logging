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
 called with args "" at "2021-11-28 14:38:10.675714-05:00".
 exception: "DO NOT PASS GO DO NOT COLLECT $200."
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/main.py", line 46, in wrapper
    output = function(*args, **kwargs)
  File "test.py", line 9, in no_return
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")
Exception: DO NOT PASS GO DO NOT COLLECT $200.

```
