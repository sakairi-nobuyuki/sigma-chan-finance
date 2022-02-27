# coding: utf-8

from sigma_chan_finance.data_structure.parameters import ExchangeRate as Parameters
import dataclasses
import numpy as np
import datetime

@dataclasses.dataclass
class ExchangeRate:

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
        #self.end = datetime.datetime.strptime(parameters.end, '%Y/%m/%d %H:%M')
        self.duration = datetime.timedelta(days=int(parameters.duration))
        self.start = self.end - self.duration