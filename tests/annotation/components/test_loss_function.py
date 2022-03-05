# coding: utf-8

from annotation.components import LossFunctions
from annotation.components import Annotation
import numpy as np

class TestLossFunctions:
    def test_calculate_gain(self, mock_one_dim_oscillating_ndarray: np.ndarray):
        loss = LossFunctions()
        annotation = Annotation(mock_one_dim_oscillating_ndarray)
        
        loss_list = []
        for extrema in annotation():
            loss_list.append(loss(mock_one_dim_oscillating_ndarray, extrema, 0.0))

        assert max(loss_list) == (mock_one_dim_oscillating_ndarray.size - 4) / 2