# coding: utf-8

import torch

from time_series_analysis.components import TimeSeriesNetworkConfig

class TestTrainRnn:
    def test_init(self):
        self.rnn = TimeSeriesNetworkConfig()
        
        assert isinstance(self.rnn.device, torch.device)