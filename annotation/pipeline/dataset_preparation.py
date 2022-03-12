# coding: utf-8
from annotation.data_structure import DatasetParameters
from annotation.io import DataLoader
from annotation.data_structure import BinaryDataset, BinaryData
from annotation.components import ExtremaAnnotation, PutCallAnnotation, DataChopper, LossFunctions
import json

class DatasetPreparation:
    def __init__(self, job_id: str, parameters_str: DatasetParameters) -> None:
        parameters_dict = json.loads(parameters_str)
        self.parameters = DatasetParameters(**parameters_dict)
        self.train_data_path = f'dataset/annotation/{job_id}/train'
        self.validation_data_path = f'dataset/annotation/{job_id}/validation'
        self.test_data_path = f'dataset/annotation/{job_id}/test'

    def __call__(self, job_id: str, parameters_str: DatasetParameters) -> None:
        pass

    def dataset_preparation(self):
        ### load data
        data_loader = DataLoader(self.parameters)
        self.source_list = data_loader.load_data()
        
        ### dataset decralation
        dataset = BinaryDataset()
        extrema = ExtremaAnnotation()
        put_call = PutCallAnnotation()
        loss = LossFunctions()

        for source in self.source_list:
            ### full length data annotation
            extrema_combination = extrema.obtain_extrema_combinations(extrema.obtain_maxima_minima(source))
            annotation = put_call(source, extrema_combination)
            data_chopper = DataChopper(source, extrema_combination, self.parameters)
            
            for i_chop in data_chopper.generate_data_chopping_parameters():
                small_source = data_chopper.chop_array(source, i_chop)
                small_annotation = data_chopper.chop_array(annotation, i_chop)
                small_loss = loss.calculate_gain_binary_annotation(small_loss, small_annotation, self.parameters.dataset_spec.offer_cost)
                data = BinaryData(small_source, small_annotation, small_annotation[-1], small_loss)

                dataset.append_random(data, self.parameters)

        return dataset

    def load_dataset(self):
        pass

    def save_dataset(self, dataset: BinaryDataset):
        pass
