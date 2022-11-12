from datetime import datetime

from mypal.models.mypal.enums import MISSING, UNKNOWN

def str_to_datetime(string: str) -> datetime:
    if isinstance(string, (MISSING, UNKNOWN)) or string is None:
        return string
    if "T" not in string:
        return short_std(string)
    else:
        return long_std(string)


def short_std(string) -> datetime:
    return datetime.strptime(string, "%Y-%m-%d")

def long_std(string) -> datetime:
    t = string.split("T")
    return datetime.strptime(
        f"{t[0]} {t[1][:-6]}",
        "%Y-%m-%d %H:%M:%S"
    )