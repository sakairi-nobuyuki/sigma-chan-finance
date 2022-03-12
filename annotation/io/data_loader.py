# coding: utf-8


from annotation.data_structure import DatasetParameters
import numpy as np
import os
from typing import Any
from pathlib import Path
import glob

class DataLoader:
    def __init__(self, parameters: DatasetParameters) -> None:
        if not isinstance(parameters, DatasetParameters):
            raise Exception(f"Dataset parameter instance is not valid")

        self.working_dir = os.path.normpath(os.path.abspath(__file__))
        self.data_dir = os.path.normpath(os.path.join(self.working_dir, '../../../' + parameters.source_dir))
        self.data_file_list = self._obtain_data_file_list()

    def __call__(self) -> Any:
        return self.load_data()

    def load_data(self) -> None:
        array_list = []
        for file in self.data_file_list:
            array = np.load(file) 
            if not self._validate_array(array):
                continue
            array_list.append(array)

        if len(array_list) == 0:
            raise ValueError(f'Length of annotation source array list is 0.')

        return array_list

    def _validate_array(self, array: np.ndarray) -> bool:
            if array.ndim != 1:
                return False
            if array.size == 0:
                return False
            return True


    def _obtain_data_file_list(self) -> list:
        return glob.glob(str(self.data_dir) + "/**/*.npy", recursive=True)
        
        
        
        