# coding: utf-8


from sigma_chan_finance.data_structure.data_classes import DataReader as DataClass
from sigma_chan_finance.io import DataReader as InputOutput



class DataReader:
    def __init__(self) -> None:
        pass

    def __call__(self, io: InputOutput, data_class: DataClass) -> None:
        data_df = io.read_data(data_class)
        data_df = io.fill_dropped_date_value_by_upwind_value(data_df)
        data_array = io.extract_values_as_ndarray(data_class, data_df)
        io.save_values_as_ndarray(data_array, data_class.data_save_path)
        

