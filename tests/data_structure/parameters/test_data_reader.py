# coding: utf-8


from sigma_chan_finance.data_structure.parameters import DataReader
import pytest




class TestDataReader:
    def test_init(self, mock_exchange_rate_parameter):

        parameters = DataReader(**mock_exchange_rate_parameter)

        assert parameters.source == mock_exchange_rate_parameter['source']
        assert parameters.target == mock_exchange_rate_parameter['target']

    def test_target_validator(self, mock_exchange_rate_parameter):

        mock_exchange_rate_parameter['target'] = 'PHP'

        with pytest.raises(ValueError): 
            parameters = DataReader(**mock_exchange_rate_parameter)