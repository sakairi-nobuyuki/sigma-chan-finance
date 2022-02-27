# coding: utf-8

from abc import ABCMeta, abstractmethod
from typing import Any
from sigma_chan_finance.data_structure.data_classes import ExchangeRate as Input
from pandas_datareader import data as pdr

    


class ExchangeRateFred:
#class ExchangeRateFred(AbstractExchangeRate):
    def __init__(self, intput: Input) -> None:
        pass
#        if input.source != 'fred':
#            raise ValueError(f'Unsuitable target against data read from FRED: {input.source}')

    def __call__(self, input: Input):
        return pdr.DataReader(input.target, input.source, input.start, input.end)