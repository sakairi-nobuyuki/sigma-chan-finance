# coding: utf-8

from annotation.data_structure import AbstractData, BinaryData, AbstractDataset, BinaryDataset, dataset_parameters
from annotation.data_structure import DatasetParameters
import numpy as np

class TestBinaryData:
    def test_init(self):
        dummy_array = np.array([0, 1, 2])
        data = BinaryData(dummy_array, 2 * dummy_array, 1)
        
        np.testing.assert_array_equal(data.source, dummy_array)
        np.testing.assert_array_equal(data.annotation, 2 * dummy_array)
        assert data.res == 1

class TestBinaryDataclass:
    def test_init(self, mock_dataset_parameters):
        dummy_array = np.array([0, 1, 2])
        binary_dataset = BinaryDataset()
        dataset_parameters = DatasetParameters(**mock_dataset_parameters)

        for i in range(1, 10, 1):
            data = BinaryData(i * dummy_array, 1.5 * i * dummy_array, 1)
            binary_dataset.append_random(data, dataset_parameters)

        assert len(binary_dataset.train) > 3
        assert len(binary_dataset.validation) == 9 - len(binary_dataset.train) - len(binary_dataset.test)