# coding: utf-8

import numpy as np
from data_reader.pipeline import DataReaderPipeline
from data_reader.data_structure.parameters import DataReader as DataReaderParameters

class TestDataReaderPipeline:
    def test_init(self, mock_exchange_rate_parameter):

        parameters = DataReaderParameters(**mock_exchange_rate_parameter)
        data_reader = DataReaderPipeline(parameters)
        tensor = data_reader.prepare_data_tensor()
        print(tensor)
        print(np.zeros((1, 3, 1)))
        assert isinstance(data_reader, DataReaderPipeline)
        