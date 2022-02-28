# coding: utf-8

from sigma_chan_finance.data_structure.data_classes import DataReader as Input
from sigma_chan_finance.data_structure.parameters import DataReader as Parameters

from sigma_chan_finance.io import DataReader as Fx

class TestFredDataRead:
    def test_init(self, mock_exchange_rate_parameter):
        parameters = Parameters(**mock_exchange_rate_parameter)
        input = Input(parameters)

        parameters.source = 'fred'
        parameters.target = 'DEXJPUS'
        input = Input(parameters)

        print(vars(input))

        fred = Fx()
        print(fred(input))