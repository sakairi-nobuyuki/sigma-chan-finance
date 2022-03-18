# coding: utf-8


from annotation.data_structure import DatasetParameters, AbstractData, AbstractDataset, data_class
from annotation.components import DataVisualization
import os
import uuid
import numpy as np
import json
from abc import ABCMeta, abstractmethod


class AbstractDatasetStorage(ABCMeta):
    @abstractmethod
    def __init__(self, job_id: str, parameters: DatasetParameters) -> None:
        if not isinstance(parameters, DatasetParameters):
            raise Exception(f"Dataset parameter instance is not valid")

        self.parameters = parameters
        self.storage_path = f'dataset/annotation/{job_id}'
        self.train_data_path = f'dataset/annotation/{job_id}/train'
        self.validation_data_path = f'dataset/annotation/{job_id}/validation'
        self.test_data_path = f'dataset/annotation/{job_id}/test'
        self.dataset_summary_path = f'dataset/annotation/{job_id}/summary.json'
        self.vilualization = DataVisualization()

    @abstractmethod
    def save_dataset(self, dataset: AbstractDataset) -> bool:
        if not isinstance(dataset, AbstractDataset):
            raise Exception(f"Dataset instance is not valid")
        
        self.validate_directory_existence()

        self.save_data_list(dataset.train, 'train')
        self.save_data_list(dataset.validation, 'validation')
        self.save_data_list(dataset.test, 'test')

    @abstractmethod
    def save_data_list(self, data_list: list, directory_path: str, visualize_flag: bool = True) -> None:
        data_dict = {}
        for data in data_list:
            if not isinstance(data, AbstractData):
                raise TypeError(f'Data type on saving is not valid: {type(data)}')

            data_id = self.obtain_data_id()
            data_dict[data_id] = self.create_data_dict(data)
                        
            np.save(self.name_ndarray_datafile(directory_path, data_id, "source"), data.source)
            np.save(self.name_ndarray_datafile(directory_path, data_id, "annotation"), data.annotation)            
    
            if visualize_flag is True:
                self.vilualization.save_ndarray_product(data.source, data.annotation, self.name_figure(directory_path, data_id))

    @abstractmethod
    def create_data_dict(self, data: AbstractData):
        pass

    @abstractmethod
    def save_dataset_dict(self, dataset_dict: dict):
        with open(self.dataset_summary_path, 'w') as f_out:
            json.dump(dataset_dict, f_out)

    @abstractmethod
    def obtain_data_id(self) -> str:
        return str(uuid.uuid4())

    @abstractmethod
    def validate_directory_existence(self):
        if os.path.exists(self.storage_path):
            raise FileExistsError(f'Storage path {self.storage_path} already exists')

    @abstractmethod
    def name_ndarray_datafile(self, directory_path: str, data_id: str, array_type: str) -> str:
        return f'{directory_path}/{data_id}_{array_type}.npy'

    @abstractmethod
    def name_figure(self, directory_path: str, data_id: str) -> str:
        return f'{directory_path}/{data_id}.png'


class BinaryDatasetStorage(AbstractDatasetStorage):
    def __init__(self, job_id: str, parameters: DatasetParameters) -> None:
        super().__init__(job_id, parameters)

    def save_dataset(self, dataset: AbstractDataset) -> bool:
        super().save_dataset(dataset)

        
    def save_data_list(self, data_list: list, directory_path: str, visualize_flag: bool = True) -> None:
        super().save_data_list(data_list, directory_path, visualize_flag)

    def create_data_dict(self, data: AbstractData):
        data_dict = {
                "score": data.score,
                "res": data.res
            }
        return data_dict

    def save_dataset_dict(self, dataset_dict: dict):
        super().save_dataset_dict(dataset_dict)

    def validate_directory_existence(self):
        return super().validate_directory_existence()

    def obtain_data_id(self) -> str:
        return super().obtain_data_id()

    def name_ndarray_datafile(self, directory_path: str, data_id: str, array_type: str) -> str:
        return super().name_ndarray_datafile(directory_path, data_id, array_type)