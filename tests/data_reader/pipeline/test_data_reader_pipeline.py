# coding: utf-8

import numpy as np
from data_reader.pipeline import DataReaderPipeline
from data_reader.data_structure.parameters import DataReader as DataReaderParameters

class TestDataReaderPipeline:
    def test_init(self, mock_exchange_rate_parameter):

        parameters = DataReaderParameters(**mock_exchange_rate_parameter)
        data_reader = DataReaderPipeline(parameters)
        array = data_reader()
        print(array)
        assert isinstance(data_reader, DataReaderPipeline)
        assert isinstance(array, np.ndarray)