# exception-logging
Exception logging decorator, class decorator and metaclass generator. Some example usages are show below, and the corresponding log files created.

---


```py
"""Standard decorator example."""

from src.exlog.exceptlog import exception_logger

log = exception_logger("./tests/log.log", "US/Eastern")


@log
def no_return():
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")


if __name__ == "__main__":
    try:
        no_return()
    except:
        pass
```
Logs the following in `log.log`.
```
ERROR:root:no_return
  raised Exception: DO NOT PASS GO DO NOT COLLECT $200.
    called with args = (), kwargs = {}
    at 2022-03-07 23:58:09.719353-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 58, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_logger.py", line 20, in no_return
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")
Exception: DO NOT PASS GO DO NOT COLLECT $200.
```


---


```py
"""Class decorator example."""

from src.exlog.exceptlog import exception_logger_cls

log = exception_logger_cls("./tests/cls.log", "US/Eastern")

@log
class Foo:
    @classmethod
    def bar1(cls):
        raise Exception("BAR1!")
    @staticmethod
    def bar2():
        raise Exception("BAR2!")
    def bar3(self):
        raise Exception("BAR3!")


if __name__ == "__main__":
    foo = Foo()
    for method in (foo.bar1, foo.bar2, foo.bar3):
        try:
            method()
        except:
            pass
```
Logs the following in `cls.log`.
```
ERROR:root:Foo.bar1
  raised Exception: BAR1!
    called with args = ("<class '__main__.Foo'>",), kwargs = {}
    at 2022-03-07 23:58:09.763220-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 58, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_cls.py", line 21, in bar1
    raise Exception("BAR1!")
Exception: BAR1!
ERROR:root:Foo.bar2
  raised Exception: BAR2!
    called with args = (), kwargs = {}
    at 2022-03-07 23:58:09.763678-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 58, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_cls.py", line 24, in bar2
    raise Exception("BAR2!")
Exception: BAR2!
ERROR:root:Foo.bar3
  raised Exception: BAR3!
    called with args = ('<__main__.Foo object at 0x7fefc0bb5a90>',), kwargs = {}
    at 2022-03-07 23:58:09.763792-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 58, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_cls.py", line 26, in bar3
    raise Exception("BAR3!")
Exception: BAR3!
```


---


```py
"""Metaclass example."""

from src.exlog.exceptlog import exception_logger_meta

log = exception_logger_meta("./tests/meta.log", "US/Eastern")


class Base(metaclass=log):
    pass

class Foo(Base):
    @classmethod
    def bar1(cls):
        raise Exception("METABAR1!")
    @staticmethod
    def bar2():
        raise Exception("METABAR2!")
    def bar3(self):
        raise Exception("METABAR3!")


if __name__ == "__main__":
    foo = Foo()
    for method in (foo.bar1, foo.bar2, foo.bar3):
        try:
            method()
        except:
            pass
```
Logs the following in `meta.log`.
```
ERROR:root:Foo.bar1
  raised Exception: METABAR1!
    called with args = ("<class '__main__.Foo'>",), kwargs = {}
    at 2022-03-07 23:58:09.825886-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 58, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_meta.py", line 24, in bar1
    raise Exception("METABAR1!")
Exception: METABAR1!
ERROR:root:Foo.bar2
  raised Exception: METABAR2!
    called with args = (), kwargs = {}
    at 2022-03-07 23:58:09.826440-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 58, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_meta.py", line 27, in bar2
    raise Exception("METABAR2!")
Exception: METABAR2!
ERROR:root:Foo.bar3
  raised Exception: METABAR3!
    called with args = ('<__main__.Foo object at 0x7fd52f27d490>',), kwargs = {}
    at 2022-03-07 23:58:09.826569-05:00
Traceback (most recent call last):
  File "/home/ryan/exception-logging-decorator/src/exlog/exceptlog.py", line 58, in wrapper
    output = function(*args, **kwargs)
  File "./tests/test_meta.py", line 29, in bar3
    raise Exception("METABAR3!")
Exception: METABAR3!
```
