# coding: utf-8

from sigma_chan_finance.data_structure import parameters
from sigma_chan_finance.data_structure.parameters import DataReader as Parameters
from sigma_chan_finance.data_structure.data_classes import AbstractDataReader
import dataclasses
import numpy as np
import datetime

@dataclasses.dataclass
class DataReader(AbstractDataReader):

    source: str
    target: str
    start: datetime
    end: datetime
    duration: datetime.timedelta
    values: np.ndarray
    data_save_path: str

    def __init__(self, parameters: Parameters) -> None:
        self.source = parameters.source
        self.target = parameters.target
        self.end = self.validate_end(parameters)
        self.duration = datetime.timedelta(days=int(parameters.duration))
        self.start = self.end - self.duration
        self.data_save_path = parameters.data_save_path

    def validate_end(self, parameters: Parameters) -> datetime:
        if parameters.end == '':
            return datetime.datetime.now()
        else:
            return datetime.datetime.strptime(parameters.end, '%Y/%m/%d')


