# coding: utf-8

from abc import ABCMeta, abstractmethod
from typing import Any
from sklearn.cluster import KMeans
import numpy as np

class OneDimClustering(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def fit(self, source: np.ndarray) -> np.ndarray:
        pass
    
    @abstractmethod
    def create_representative_set(self, source: np.ndarray, labels: np.ndarray) -> Any:
        pass

    @abstractmethod
    def obtain_number_of_clusters(self, source: np.ndarray, cluster_size: int = 4) -> int:
        if source.ndim == 1:
            return int(source.size / cluster_size)
        else:
            raise Exception(f"On clustering extremas, input array must be one dimensional")
        

class OneDimKNN(OneDimClustering):
    def __init__(self) -> None:
        super().__init__()

    def fit(self, source: np.ndarray, cluster_size: int = 4) -> np.ndarray:
        model = KMeans(n_clusters = self.obtain_number_of_clusters(source, cluster_size), random_state = 10)
        knn_input = (source * 100).astype(int).reshape(-1, 1)
        print(knn_input)
        model.fit(knn_input)

        return model.labels_


    def create_representative_set(self, source: np.ndarray, labels: np.ndarray) -> Any:
        pass

    def obtain_number_of_clusters(self, source: np.ndarray, cluster_size: int = 4) -> int:
        return super().obtain_number_of_clusters(source, cluster_size)