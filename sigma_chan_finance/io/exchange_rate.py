# coding: utf-8

from abc import ABCMeta, abstractmethod
from typing import Any
from sigma_chan_finance.data_structure.data_classes import ExchangeRate as Input
from pandas_datareader import data as pdr

    


class ExchangeRate:

    def __call__(self, input: Input):

        return pdr.DataReader(input.target, input.source, input.start, input.end)