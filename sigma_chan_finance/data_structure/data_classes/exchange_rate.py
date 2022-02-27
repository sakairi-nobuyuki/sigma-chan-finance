# coding: utf-8

from sigma_chan_finance.data_structure.parameters import ExchangeRate as Parameters
from sigma_chan_finance.data_structure.data_classes import AbstractDataClass
import dataclasses
import numpy as np
import datetime

@dataclasses.dataclass
class ExchangeRate(AbstractDataClass):

    source: str
    target: str
    start: datetime
    end: datetime
    duration: datetime.timedelta
    values: np.ndarray

    def __init__(self, parameters: Parameters) -> None:
        self.source = parameters.source
        self.target = parameters.target
        self.end = datetime.datetime.strptime(parameters.end, '%Y/%m/%d')
        self.duration = datetime.timedelta(days=int(parameters.duration))
        self.start = self.end - self.duration