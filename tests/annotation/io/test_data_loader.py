# coding: utf-8

from annotation.io import DataLoader
from annotation.data_structure import DatasetParameters
import pytest


class TestDataLoader:
    def test_init(self, mock_dataset_parameters):
        parameters = DatasetParameters(**mock_dataset_parameters)
        data_loader = DataLoader(parameters)

        print(data_loader.working_dir)
        print(data_loader.data_dir)
        print(data_loader.data_file_list)

    def test_init(self, mock_dataset_parameters):
        parameters = DatasetParameters(**mock_dataset_parameters)
        data_loader = DataLoader(parameters)
        

        array_list = data_loader.load_data()

        print(array_list[0])

        assert len(array_list) > 0
        assert array_list[0].ndim > 0