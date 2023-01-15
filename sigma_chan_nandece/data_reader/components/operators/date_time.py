# coding: utf-8

import datetime


def get_date_in_str(n_days_later: int = None) -> str:
    """
    Args:
        n_days_later: int: 
    Returns:
        date: str:
            Date ins str n_days_later. If n_days_later in args, is none, today is returned.
    """
    if n_days_later is None:
        return str(datetime.datetime.now().strftime("%Y/%m/%d"))
    else:
        return str((datetime.datetime.now() + datetime.timedelta(days=n_days_later)).strftime("%Y/%m/%d"))