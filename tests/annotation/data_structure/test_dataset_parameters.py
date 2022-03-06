# coding: utf-8

from annotation.data_structure import DatasetDirectoryParameters, DatasetCreationParameters, DatasetParameters


class TestDatasetCreationParameters:
    def test_dataset_creation_parameters(self, mock_dataset_parameters):
        parameters = DatasetParameters(**mock_dataset_parameters)
        assert parameters.dataset_spec.length == mock_dataset_parameters["dataset_spec"]["length"]
        assert parameters.dataset_spec.offer_cost == mock_dataset_parameters["dataset_spec"]["offer_cost"]