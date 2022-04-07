# coding: utf-8

import torch

from train.components import TimeSeriesTrainConfig

class TestTrainRnn:
    def test_init(self):
        self.rnn = TimeSeriesTrainConfig()
        
        assert isinstance(self.rnn.device, torch.device)