##############################################################
# KEEP FIRST! # RUN TEST ONE DIR UP!
##############################################################
import pathlib
import sys

tests_path = str(pathlib.Path(__file__).absolute().parent.parent)
sys.path.insert(0, tests_path)
##############################################################

from typing import NoReturn

from src.exceptlog.main import exception_logger

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
