# coding: utf-8

from webbrowser import get
from data_reader.components.operators import get_date_in_str
import datetime

def test_get_date_in_str():

    print("today: ", get_date_in_str())
    assert get_date_in_str() == str(datetime.datetime.now().strftime("%Y/%m/%d"))
    
    print("10 days later: ", get_date_in_str(10))
    assert get_date_in_str(10) == str((datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%Y/%m/%d"))
    
    print("10 days ago: ", get_date_in_str(-10))
    assert get_date_in_str(-10) == str((datetime.datetime.now() + datetime.timedelta(days=-10)).strftime("%Y/%m/%d"))