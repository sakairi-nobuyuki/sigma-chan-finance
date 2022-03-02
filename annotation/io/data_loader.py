# coding: utf-8

from annotation.data_structure import AnnotationDataClass
import numpy as np
import os
from typing import Any
from pathlib import Path
import glob

class DataLoader:
    def __init__(self) -> None:
        self.working_dir = os.path.normpath(os.path.abspath(__file__))
        self.data_dir = os.path.normpath(os.path.join(self.working_dir, '../../../data'))
        self.data_file_list = self._obtain_data_file_list()

    def __call__(self) -> Any:
        return self.load_data()

    def load_data(self) -> None:
        array_list = []
        for file in self.data_file_list:
            array = np.load(file) 
            if array.size == 0:
                continue
            array_list.append(array)

        return array_list

    

    def _obtain_data_file_list(self) -> list:
        return glob.glob(str(self.data_dir) + "/**/*.npy", recursive=True)
        
        
        
        