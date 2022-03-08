##############################################################
# KEEP FIRST! # RUN TEST ONE DIR UP!
##############################################################
import pathlib
import sys

tests_path = str(pathlib.Path(__file__).absolute().parent.parent)
sys.path.insert(0, tests_path)
##############################################################

"""Class decorator example."""

from typing import NoReturn

from src.exlog.exceptlog import exception_logger_cls

log = exception_logger_cls("./tests/cls.log", "US/Eastern")

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
