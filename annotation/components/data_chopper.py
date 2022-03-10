# coding: utf-8

from annotation.data_structure import DatasetCreationParameters
import numpy as np
import random

class DataChopper:
    def __init__(self, source: np.ndarray, extrema: list, parameters: DatasetCreationParameters) -> None:
        self.chop_length = parameters.length
        self.n_source = source.size
        self.n_chop_max = extrema[-1] - extrema[0] - parameters.length
        self.n_chop = min(self.n_chop_max, parameters.number_of_data)
        self.i_chop_upper  = extrema[-1] - parameters.length
        self.i_chop_bottom = extrema[0]
        
        self.info()

    def generate_small_arrays(self, array: np.ndarray, chop_pos_list: list):
        i = 0
        while True:
            print("in the generator: ", array, chop_pos_list)
            print("in the generator : ", array[chop_pos_list[i] + self.chop_length])
            yield array[chop_pos_list[i] + self.chop_length]
            i += 1

    def chop_array(self, array: np.ndarray, i_chop_left: int):
        if array.ndim != 1:
            raise Exception(f"Array dimension is not correct during dataset creation")
        if array.size < self.i_chop_upper:
            raise Exception(f"Array is too small")

        return array[i_chop_left:i_chop_left + self.chop_length]

    def generate_data_chopping_parameters(self) -> list:
        return random.sample(range(self.i_chop_bottom, self.i_chop_upper), self.n_chop)


    def info(self) -> None:
        print("In dataset preparation from data:")
        print(f"  Length of the source: {self.n_source}")
        print(f"  Length of the small array: {self.chop_length}")
        print(f"  Max number of data in the dataset: {self.n_chop_max}")
        print(f"  Number of data in the dataset: {self.n_chop}")