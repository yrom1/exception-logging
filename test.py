from typing import NoReturn

from exception_logger.main import log

@log
def no_return() -> NoReturn:
    """Test function."""
    raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")


if __name__ == "__main__":
    try:
        no_return()
    except:
        pass
