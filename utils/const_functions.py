import time
from datetime import datetime
import pytz
from data.config import BOT_TIMEZONE


######################################## MISC ########################################
# Getting date
def get_date(full: bool = True) -> str:
    if full:  # full date with time
        return datetime.now(pytz.timezone(BOT_TIMEZONE)).strftime("%d.%m.%Y %H:%M:%S")
    else:  # only date, without time
        return datetime.now(pytz.timezone(BOT_TIMEZONE)).strftime("%d.%m.%Y")


# Getting date for dbx
def get_date_for_tables(full: bool = True) -> str:
    if full:  # full date with time
        return datetime.now(pytz.timezone(BOT_TIMEZONE)).strftime("%d.%m.%Y %H:%M:%S")
    else:  # only date, without time
        return datetime.now(pytz.timezone(BOT_TIMEZONE)).strftime("%d_%m_%Y")


# Getting unix time
def get_unix(full: bool = False) -> int:
    if full:
        return time.time_ns()
    else:
        return int(time.time())


# Clearing text from HTML tags
def clear_html(get_text: str) -> str:
    if get_text is not None:
        if "<" in get_text: get_text = get_text.replace("<", "*")
        if ">" in get_text: get_text = get_text.replace(">", "*")
    else:
        get_text = ""

    return get_text