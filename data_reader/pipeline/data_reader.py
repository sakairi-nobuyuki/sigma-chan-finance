# coding: utf-8

from typing import Any
from data_reader.data_structure.parameters import DataReader as DataReaderParameters
from data_reader.data_structure.data_classes import DataReader as DataClass
from data_reader.io import DataReader as InputOutput


class DataReader:
    def __init__(self) -> None:
        pass

    def __call__(self, io: InputOutput, data_class: DataClass) -> None:
        data_df = io.read_data(data_class)
        data_df = io.fill_dropped_date_value_by_upwind_value(data_df)
        data_array = io.extract_values_as_ndarray(data_class, data_df)
        
        return data_array
        
        
class DataReaderPipeline:
    def __init__(self, parameters: DataReaderParameters) -> None:
        self.data_class = DataClass(parameters)
        self.io = InputOutput()

    def __call__(self) -> Any:
    #def __call__(self, *args: Any, **kwds: Any) -> Any:
        data_df = self.io.read_data(self.data_class)
        data_df = self.io.fill_dropped_date_value_by_upwind_value(data_df)
        data_aarray = self.io.extract_values_as_ndarray(self.data_class, data_df)

        return data_aarray