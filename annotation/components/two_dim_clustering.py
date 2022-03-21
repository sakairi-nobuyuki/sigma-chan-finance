# coding: utf-8

from abc import ABCMeta, abstractmethod
from typing import Any
from sklearn.cluster import KMeans
import numpy as np

class TwoDimClustering(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def fit(self, src_rate: np.ndarray, src_pos: np.ndarray, cluster_size: int = 4) -> np.ndarray:
        pass

    def create_representative_set(self, source: np.ndarray, labels: np.ndarray) -> Any:
        pass

    @abstractmethod
    def obtain_number_of_clusters(self, source: np.ndarray, cluster_size: int = 4) -> int:
        if source.ndim == 1:
            return int(source.size / (1 * cluster_size))
        else:
            raise Exception(f"On clustering extremas, input array must be one dimensional")
        

class TwoDimKNN(TwoDimClustering):
    def __init__(self) -> None:
        super().__init__()

    

    def fit(self, src_rate: np.ndarray, src_pos: np.ndarray, cluster_size: int = 4) -> np.ndarray:
        src_rate_input = (src_rate * 100).astype(int)
        knn_input = np.stack([src_rate_input, src_pos], 1)
        print(knn_input)
        n_clusters= self.obtain_number_of_clusters(src_rate, cluster_size)
        model = KMeans(n_clusters = n_clusters, random_state = 10)
        
        model.fit(knn_input)

        return model.labels_



    def obtain_number_of_clusters(self, source: np.ndarray, cluster_size: int = 4) -> int:
        return super().obtain_number_of_clusters(source, cluster_size)