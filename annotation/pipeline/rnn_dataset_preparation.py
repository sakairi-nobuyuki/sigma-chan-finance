# coding: utf-8

from annotation.data_structure import DatasetParameters
from annotation.components import DataChopper
from annotation.io import DataLoader
import numpy as np

class RnnDatasetPreparation:
    def __init__(self, parameters: DatasetParameters) -> None:
        self.x_day = 5
        self.parameters = parameters
        self.data_loader = DataLoader(self.parameters)
        self.data_list = self.data_loader()
        

        ### initialize data chopper 
        self.data_range_array = np.array([
            self.x_day, self.data_list[0].size - parameters.dataset_spec.number_of_data 
            ])
        self.data_chopper = DataChopper(self.data_list[0], self.data_range_array, parameters.dataset_spec)

        ### minor data preparation
        self.chop_pos_list = self.data_chopper.generate_data_chopping_parameters()
        

    def create_minor_array_list(self, array: np.ndarray) -> list:

        train_array_list = []
        correct_data_list = []
        for i in range(self.parameters.dataset_spec.number_of_data):
            train_array_list.append(self.data_chopper.chop_array(array, self.chop_pos_list[i]))
            correct_data_list.append(array[self.chop_pos_list[i] + self.parameters.dataset_spec.length + self.x_day])

        return train_array_list, correct_data_list
    



