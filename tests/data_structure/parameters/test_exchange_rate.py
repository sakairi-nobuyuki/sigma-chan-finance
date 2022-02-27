# coding: utf-8


from sigma_chan_finance.data_structure.parameters import ExchangeRate
import pytest


@pytest.fixture(scope='session')
def mock_parameter():
    parameter_dict = {
        'source': 'yahoo_finance',
        'target': 'USD',
        'end': '2022/02/27 12:05',
        'duration': '100'
    }
    return parameter_dict


class TestExchangeRate:
    def test_init(self, mock_parameter):

        parameters = ExchangeRate(**mock_parameter)

        assert parameters.source == mock_parameter['source']
        assert parameters.target == mock_parameter['target']

    def test_target_validator(self, mock_parameter):

        mock_parameter['target'] = 'PHP'

        with pytest.raises(ValueError): 
            parameters = ExchangeRate(**mock_parameter)