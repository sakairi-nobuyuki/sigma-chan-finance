# coding: utf-8

from annotation.components import LossFunctions, LossFunctionsSingleArg
from annotation.components import ExtremaAnnotation, PutCallAnnotation, MoreBetterPattern
import numpy as np

class TestLossFunctions:
    def test_calculate_gain(self, mock_one_dim_oscillating_ndarray: np.ndarray):
        loss = LossFunctions()
        annotation = ExtremaAnnotation()
        
        loss_list = []
        for extrema in annotation(mock_one_dim_oscillating_ndarray):
            loss_list.append(loss(mock_one_dim_oscillating_ndarray, extrema, 0.0))

        assert max(loss_list) == (mock_one_dim_oscillating_ndarray.size - 4) / 2

    def test_calculate_gain_binary_annotation(self, mock_one_dim_oscillating_ndarray: np.ndarray):
        loss = LossFunctions()
        annotation = ExtremaAnnotation()
        put_call = PutCallAnnotation()
        
        loss_list = []
        for extrema in annotation(mock_one_dim_oscillating_ndarray):
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


    def test_obtain_delta(self):
        mock_annotation = np.array([0, 0, 1, 1, 1, 0, 0])
        delta           = np.array([0, 0, -1, 0, 1, 0, 0])
        loss = LossFunctions()

        np.testing.assert_array_equal(loss.obtain_delta(mock_annotation), delta)

    def test_obtain_up_down(self):
        mock_annotation = np.array([0, 1, 1, 0, 1, 1])
        loss = LossFunctions()
        
        assert loss.obtain_up_down(mock_annotation) == 2

    def test_calculate_gain_binary_annotation(self):
        mock_annotation = np.array([0,   1,   1,   0,   0,   1,   1,   1])
        mock_source     = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])

        loss = LossFunctions()
        
        np.testing.assert_array_equal(loss.obtain_delta(mock_annotation), np.array([0, -1, 1, 0, 0, -1, 0, 1]))
        assert loss.calculate_gain_binary_annotation(mock_source, mock_annotation, 2) == -1.0

class TestLossFunctionsSingleArg:
    def test_init(self, mock_ndarray_for_cluster):
        
        loss_1a = LossFunctionsSingleArg(mock_ndarray_for_cluster, mock_ndarray_for_cluster, 0.1, ExtremaAnnotation)
        extrema_annotation = MoreBetterPattern(loss_1a)
        
    def test_calculate_gain(self):
        pass