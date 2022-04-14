# coding: utf-8

from annotation.components.data_chopper import DataChopper
from annotation.pipeline import RnnDatasetPreparation
from annotation.data_structure import DatasetParameters

class TestRnnDatasetPreparation:
    def test_init(self, mock_dataset_parameters):
        parameters = DatasetParameters(**mock_dataset_parameters)
        rnn_dataset = RnnDatasetPreparation(parameters)

        print("data length: ", rnn_dataset.data_list[0].size)
        print("data range: ", rnn_dataset.data_range_array[-1] - rnn_dataset.data_range_array[0], rnn_dataset.data_range_array[-1], rnn_dataset.data_range_array[0])
        print("minor data range: ", rnn_dataset.chop_pos_list)
        print("max data chop point: ", max(rnn_dataset.chop_pos_list))

        assert rnn_dataset.data_list[0].size > rnn_dataset.data_range_array[-1] - rnn_dataset.data_range_array[0]
        assert len(rnn_dataset.chop_pos_list) == parameters.dataset_spec.number_of_data
        assert max(rnn_dataset.chop_pos_list) < rnn_dataset.data_list[0].size - parameters.dataset_spec.number_of_data - parameters.dataset_spec.length
        assert isinstance(rnn_dataset.data_chopper, DataChopper)


    def test_create_minor_array_list(self, mock_dataset_parameters):
        parameters = DatasetParameters(**mock_dataset_parameters)
        rnn_dataset = RnnDatasetPreparation(parameters)

        print(rnn_dataset.create_minor_array_list(rnn_dataset.data_list[0]))