# coding: utf-8

from annotation.components import LossFunctions
from annotation.components import ExtremaAnnotation, PutCallAnnotation
import numpy as np

class TestLossFunctions:
    def test_calculate_gain(self, mock_one_dim_oscillating_ndarray: np.ndarray):
        loss = LossFunctions()
        annotation = ExtremaAnnotation(mock_one_dim_oscillating_ndarray)
        
        loss_list = []
        for extrema in annotation():
            loss_list.append(loss(mock_one_dim_oscillating_ndarray, extrema, 0.0))

        assert max(loss_list) == (mock_one_dim_oscillating_ndarray.size - 4) / 2

    def test_calculate_gain_binary_annotation(self, mock_one_dim_oscillating_ndarray: np.ndarray):
        loss = LossFunctions()
        annotation = ExtremaAnnotation(mock_one_dim_oscillating_ndarray)
        put_call = PutCallAnnotation()
        
        loss_list = []
        for extrema in annotation():
            binary_annotation = put_call(mock_one_dim_oscillating_ndarray, extrema)
            loss_list.append(
                loss.calculate_gain_binary_annotation(
                    mock_one_dim_oscillating_ndarray, 
                    binary_annotation,
                    extrema, 
                    0.0
                )
            )

        assert max(loss_list) == (mock_one_dim_oscillating_ndarray.size - 4) / 2        