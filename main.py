"""Exception logging decorator."""

import datetime
import functools
import logging
import sys

if (sys.version_info.major, sys.version_info.minor) < (3, 6):
    raise Exception("Must be using Python 3.6 or higher for zoneinfo.")
elif sys.version_info.minor < 9:
    import backports.zoneinfo
else:
    import zoneinfo  # type: ignore

logging.basicConfig(filename="log.log", filemode="a", level=logging.ERROR)
LOGGER = logging.getLogger()


def log(function):
    """Exception logging decorator.
    Uses "US/Eastern" time zone by default, for other zones see:
        https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        https://www.python.org/dev/peps/pep-0615/"""

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        timestamp = str(
            datetime.datetime.now().astimezone(
                backports.zoneinfo.ZoneInfo("US/Eastern")
            )
        )
        signature = ", ".join(args_repr + kwargs_repr)
        try:
            output = function(*args, **kwargs)
            return output
        except Exception as e:
            LOGGER.exception(
                f'Exception raised in function "{function.__qualname__}" called with args ->{signature}<- at "{timestamp}". exception: {str(e)}'
            )
            raise e

    return wrapper
