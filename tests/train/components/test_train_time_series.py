# coding: utf-8

import torch

from train.components import TimeSeriesTrain

class TestTrainRnn:
    def test_init(self):
        self.rnn = TimeSeriesTrain()
        
        assert isinstance(self.rnn.device, torch.device)