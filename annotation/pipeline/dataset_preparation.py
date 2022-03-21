# coding: utf-8

from annotation.data_structure import DatasetParameters
from annotation.data_structure.data_class import AbstractDataset
from annotation.io import DataLoader
from annotation.data_structure import BinaryDataset, BinaryData
from annotation.components import ExtremaAnnotation, PutCallAnnotation, DataChopper, LossFunctions
import json

from annotation.io.dataset_storage import AbstractDatasetStorage

class DatasetPreparation:
    def __init__(self, job_id: str, parameters_str: DatasetParameters) -> None:
        parameters_dict = json.loads(parameters_str)
        self.job_id = job_id
        self.parameters = DatasetParameters(**parameters_dict)
        

    def __call__(self, job_id: str, parameters_str: DatasetParameters) -> None:
        pass

    def dataset_preparation(self):
        ### load data
        data_loader = DataLoader(self.parameters)
        print("Data loading")
        self.source_list = data_loader.load_data()
        print(f"  Length of source ndarray list: {len(self.source_list)}")

        ### dataset decralation
        print("Initializing")
        dataset = BinaryDataset()
        extrema = ExtremaAnnotation()
        put_call = PutCallAnnotation()
        loss = LossFunctions()

        print("Start dataset preparation")
        for source in self.source_list:
            ### full length data annotation
            print("  Annotating extrema in given source data")
            maxima_minima = extrema.obtain_maxima_minima(source)
            print(f"  number of extrema: {maxima_minima.size}")
            print("  Searching best extrema combination")
            print(source)
            print(maxima_minima)
            extrema_combination = extrema.obtain_extrema_combinations(source, maxima_minima, self.parameters.dataset_spec.offer_cost)
            print("  Annotating put or call")
            annotation = put_call(source, extrema_combination)
            print("  Divide data into fragmented small data")
            data_chopper = DataChopper(source, extrema_combination, self.parameters)
            
            for i_chop in data_chopper.generate_data_chopping_parameters():
                small_source = data_chopper.chop_array(source, i_chop)
                small_annotation = data_chopper.chop_array(annotation, i_chop)
                small_loss = loss.calculate_gain_binary_annotation(small_loss, small_annotation)
                data = BinaryData(small_source, small_annotation, small_annotation[-1], small_loss)
                

                dataset.append_random(data, self.parameters)
                

        return dataset

    def load_dataset(self):
        pass

    def save_dataset(self, dataset: AbstractDataset, dataset_storage: AbstractDatasetStorage):
        if not isinstance(dataset_storage, AbstractDatasetStorage):
            raise TypeError(f'Dataset storage type is invalid on saving dataset: {type(dataset_storage)}')
        if not isinstance(dataset, AbstractDataset):
            raise TypeError(f'Dataset type invalid on saving dataset: {type(dataset)}')

        dataset_storage.save_dataset(dataset)

def obtain_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('jod_id')
    parser.add_argument('parameters_path')

    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = obtain_args()
    with open(args.parameters_path) as f_in:
        parameters = json.load(f_in)
    parameters_str = json.dumps(parameters)
    dataset_prepare = DatasetPreparation(args.job_id, parameters_str)