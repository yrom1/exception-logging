# exception-logging-decorator
This library provides an exception logging decorator, class decorators, and metaclass. Some example usages are show below, and the corresponding log files created.

---


```py
"""Standard decorator example."""

from typing import NoReturn

from src.exlog.exceptlog import exception_logger

log = exception_logger("./tests/log.log", "US/Eastern")


@log
def no_return() -> NoReturn:
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")


if __name__ == "__main__":
    try:
        no_return()
    except:
        pass
```
Logs the following in log.log.
```
ERROR:root:no_return
  raised Exception: DO NOT PASS GO DO NOT COLLECT $200.
    called with args = (), kwargs = {}
    at 2022-03-07 23:28:57.525784-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 70, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_logger.py", line 22, in no_return
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")
Exception: DO NOT PASS GO DO NOT COLLECT $200.
```


---


```py

"""Class decorator example."""

from typing import NoReturn

from src.exlog.exceptlog import exception_logger_cls

log = exception_logger_cls("./tests/cls.log", "US/Eastern")

#test
@log
class Foo:
    @classmethod
    def bar1(cls) -> NoReturn:
        raise Exception("BAR1!")
    @staticmethod
    def bar2() -> NoReturn:
        raise Exception("BAR2!")
    def bar3(self) -> NoReturn:
        raise Exception("BAR3!")


if __name__ == "__main__":
    foo = Foo()
    for method in (foo.bar1, foo.bar2, foo.bar3):
        try:
            method()
        except:
            pass
```
Logs the following in cls.log.
```
ERROR:root:Foo.bar1
  raised Exception: BAR1!
    called with args = ('<__main__.Foo object at 0x7fd5ea30cb50>',), kwargs = {}
    at 2022-03-07 23:28:57.567867-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 70, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_cls.py", line 25, in bar1
    raise Exception("BAR1!")
Exception: BAR1!
ERROR:root:Foo.bar2
  raised TypeError: bar2() takes 0 positional arguments but 1 was given
    called with args = ('<__main__.Foo object at 0x7fd5ea30cb50>',), kwargs = {}
    at 2022-03-07 23:28:57.568329-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 70, in wrapper
    output = function(*args, **kwargs)
TypeError: bar2() takes 0 positional arguments but 1 was given
ERROR:root:Foo.bar3
  raised Exception: BAR3!
    called with args = ('<__main__.Foo object at 0x7fd5ea30cb50>',), kwargs = {}
    at 2022-03-07 23:28:57.568439-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 70, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_cls.py", line 30, in bar3
    raise Exception("BAR3!")
Exception: BAR3!
```


---


```py
"""Metaclass example."""

from typing import NoReturn

from src.exlog.exceptlog import exception_logger_meta

log = exception_logger_meta("./tests/meta.log", "US/Eastern")


class Base(metaclass=log):
    pass

class Foo(Base):
    @classmethod
    def bar1(cls) -> NoReturn:
        raise Exception("METABAR1!")
    @staticmethod
    def bar2() -> NoReturn:
        raise Exception("METABAR2!")
    def bar3(self) -> NoReturn:
        raise Exception("METABAR3!")


if __name__ == "__main__":
    foo = Foo()
    for method in (foo.bar1, foo.bar2, foo.bar3):
        try:
            method()
        except:
            pass
```
Logs the following in meta.log.
```
ERROR:root:Foo.bar1
  raised Exception: METABAR1!
    called with args = ('<__main__.Foo object at 0x7f590d321e80>',), kwargs = {}
    at 2022-03-07 23:28:57.609218-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 70, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_meta.py", line 26, in bar1
    raise Exception("METABAR1!")
Exception: METABAR1!
ERROR:root:Foo.bar2
  raised TypeError: bar2() takes 0 positional arguments but 1 was given
    called with args = ('<__main__.Foo object at 0x7f590d321e80>',), kwargs = {}
    at 2022-03-07 23:28:57.609744-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 70, in wrapper
    output = function(*args, **kwargs)
TypeError: bar2() takes 0 positional arguments but 1 was given
ERROR:root:Foo.bar3
  raised Exception: METABAR3!
    called with args = ('<__main__.Foo object at 0x7f590d321e80>',), kwargs = {}
    at 2022-03-07 23:28:57.609879-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 70, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_meta.py", line 31, in bar3
    raise Exception("METABAR3!")
Exception: METABAR3!
```
