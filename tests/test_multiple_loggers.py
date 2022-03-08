#################################################################
# KEEP FIRST! # RUN TEST ONE DIR UP!
#################################################################
import pathlib
import sys

tests_path = str(pathlib.Path(__file__).absolute().parent.parent)
sys.path.insert(0, tests_path)
#################################################################

from typing import NoReturn

from src.exlog.exceptlog import exception_logger

zonk = exception_logger("./tests/zonkers.log")
bonk = exception_logger("./tests/bonkers.log")

@zonk
def zonkers() -> NoReturn: raise Exception("zonkers!")

@bonk
def bonkers() -> NoReturn: raise Exception("bonkers!")

if __name__ == "__main__":
    for no_return in [zonkers, bonkers]:
        try:
            no_return()
        except:
            pass
