##############################################################
# KEEP FIRST! # RUN TEST ONE DIR UP!
##############################################################
import pathlib
import sys

tests_path = str(pathlib.Path(__file__).absolute().parent.parent)
sys.path.insert(0, tests_path)
##############################################################

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
