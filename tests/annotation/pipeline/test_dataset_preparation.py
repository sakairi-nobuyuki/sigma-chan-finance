# coding: utf-8

from annotation.data_structure import DatasetParameters
from annotation.pipeline import DatasetPreparation
from annotation.io import DataLoader, data_loader
import os

class TestDatasetPreparation:
    def test_init(self, mock_dataset_parameters):
        parameters = DatasetParameters(**mock_dataset_parameters)
        dataset_preparation = DatasetPreparation(parameters)
        data_loader = DataLoader(parameters)
        
        assert len(data_loader.data_file_list) > 0
        assert os.path.exists(data_loader.data_file_list[0])