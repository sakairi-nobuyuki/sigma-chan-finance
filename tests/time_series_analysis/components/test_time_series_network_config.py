# coding: utf-8

import torch
import os
import numpy as np

from time_series_analysis.components import TimeSeriesNetworkConfig

class TestTrainRnn:
    def test_init(self):
        self.rnn = TimeSeriesNetworkConfig()
        
        assert isinstance(self.rnn.device, torch.device)

    def test_load_save_model(self):
        self.rnn = TimeSeriesNetworkConfig()
        
        self.rnn.device = torch.device("cpu")

        self.model = self.rnn.compile_model()

        model_path = "test_model.pth"
        if os.path.exists(model_path):
            os.remove(model_path)
        
        self.rnn.save_model(model_path, self.model)

        assert os.path.exists(model_path)

        self.rnn2 = TimeSeriesNetworkConfig() 
        self.rnn2.device = torch.device("cpu")
        self.model2 = self.rnn2.compile_model()
        self.model2 = self.rnn2.load_model(self.model2, model_path)

        weight = self.model.network.weight_ih_l0.to("cpu").detach().numpy().copy()
        weight2 = self.model2.network.weight_ih_l0.to("cpu").detach().numpy().copy()

        np.testing.assert_array_equal(weight, weight2)


        if os.path.exists(model_path):
            os.remove(model_path)
