# coding: utf-8

import os
from abc import ABCMeta, abstractmethod
from typing import Any
from sigma_chan_finance.data_structure.data_classes import DataReader as Input
from pandas_datareader import data as pdr
import numpy as np
import pandas as pd
from pathlib import Path    


class DataReader:

    def __init__(self):
        pass

    def read_data(self, input: Input) -> pd.DataFrame:

        return pdr.DataReader(input.target, input.source, input.start, input.end)

    def fill_dropped_date(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        return data_frame.resample('D').mean()

    def fill_dropped_date_value_by_fixed_value(self, data_frame: pd.DataFrame, fixed_value: float) -> pd.DataFrame:
        data_frame = self.fill_dropped_date(data_frame)
        return data_frame.fillna(fixed_value)

    def fill_dropped_date_value_by_upwind_value(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        data_frame = self.fill_dropped_date(data_frame)
        return data_frame.fillna(method='ffill')
        
    def extract_values_as_ndarray(self, input: Input, data_frame: pd.DataFrame) -> np.ndarray:
        return data_frame[input.target].values

    def save_values_as_ndarray(self, array: np.ndarray, file_path: str) -> bool:
        if not isinstance(array, np.ndarray):
            raise ValueError(f'DataReader array to save must be np.ndarray: {type(array)}')
        self._validate_file_existence(file_path)
        
        np.save(file_path, array)

        return self._validate_save_file(file_path)

    def save_data_frame(self, data_frame: pd.DataFrame, file_path: str) -> bool:
        if not isinstance(data_frame, pd.DataFrame):
            raise ValueError(f'DataReader DataFrame data to save must be pd.DataFrame: {type(data_frame)}')
        self._validate_file_existence(file_path)

        data_frame.to_csv(Path(file_path))

        return self._validate_save_file(file_path)

    def _validate_file_existence(self, file_path: Input) -> None:
        if os.path.exists(Path(file_path)):
            raise FileExistsError(f'DataReader file already exists: {file_path}')
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

    def _validate_save_file(self, file_path: str) -> bool:
        if os.path.exists(Path(file_path)):
            return True
        else:
            return False