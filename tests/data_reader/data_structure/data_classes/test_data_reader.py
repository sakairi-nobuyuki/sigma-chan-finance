# coding: utf-8

from datetime import datetime, timedelta


from data_reader.data_structure.data_classes import DataReader as Input
from data_reader.data_structure.parameters import DataReader as Parameters

class TestDataReader:
    def test_init(self, mock_exchange_rate_parameter):
        parameters = Parameters(**mock_exchange_rate_parameter)
        input = Input(parameters)

        assert input.source == mock_exchange_rate_parameter['source']
        assert input.target == mock_exchange_rate_parameter['target']
        date_list = mock_exchange_rate_parameter['end'].split('/')
        assert input.end == datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        duration = mock_exchange_rate_parameter['duration']
        assert input.duration == timedelta(days=int(duration))
        assert input.start == datetime(int(date_list[0]), int(date_list[1]), int(date_list[2])) - timedelta(days=int(duration))
