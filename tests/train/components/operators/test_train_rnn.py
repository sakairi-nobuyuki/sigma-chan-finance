# coding: utf-8

import torch

from train.components.operators import TrainRnn

class TestTrainRnn:
    def test_init(self):
        self.rnn = TrainRnn()
        
        assert isinstance(self.rnn.device, torch.device)