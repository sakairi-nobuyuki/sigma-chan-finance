# coding: utf-8

from typing import Any
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class VisualizationSingleton(type):
    _instance = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwds)
            cls._instance[cls] = instance
        return cls._instance[cls]

class DataVisualization(metaclass=VisualizationSingleton):

    def __init__(self) -> None:
        pass

    def save_ndarray_product(self, array_1: np.ndarray, array_2: np.ndarray, file_path: str) -> None:
        sns.lineplot(array_1 * array_2)
        plt.savefig(file_path)
        
        