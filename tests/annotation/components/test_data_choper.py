# coding: utf-8


from annotation import data_structure
from annotation.components import DataChopper
from annotation.data_structure import DatasetCreationParameters
import pytest


class TestDataChopper:
    def test_init(self, mock_dataset_creation_parameters, mock_one_dim_oscillating_ndarray):
        parameters = DatasetCreationParameters(**mock_dataset_creation_parameters)
        parameters.length = 3
        parameters.number_of_data = 2
        extrema = [2, 5, 7]
        data_chopper = DataChopper(mock_one_dim_oscillating_ndarray, extrema, parameters)
        chop_pos_list =  data_chopper.generate_data_chopping_parameters()

        assert data_chopper.n_chop == 2
        assert data_chopper.i_chop_upper == 4
        assert data_chopper.i_chop_bottom == 2
        assert data_chopper.chop_array(mock_one_dim_oscillating_ndarray, extrema[chop_pos_list[0]]).size > 0


    def test_generator(self, mock_dataset_creation_parameters, mock_one_dim_oscillating_ndarray):
        parameters = DatasetCreationParameters(**mock_dataset_creation_parameters)
        parameters.length = 3
        parameters.number_of_data = 2
        extrema = [2, 5, 7]
        data_chopper = DataChopper(mock_one_dim_oscillating_ndarray, extrema, parameters)
        chop_pos_list =  data_chopper.generate_data_chopping_parameters()

        small_array_generator = data_chopper.generate_small_arrays(mock_one_dim_oscillating_ndarray, chop_pos_list)
        print(small_array_generator)
        print(small_array_generator.__next__()) 