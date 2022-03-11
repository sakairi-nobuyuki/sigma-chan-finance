# coding: utf-8

import numpy as np

class LossFunctions:
    def __init__(self) -> None:
        pass
        
    def __call__(self, source: np.ndarray, extrema: np.ndarray, offer_cost: float) -> float:
        return self.calculate_gain(source, extrema, offer_cost)

    def calculate_gain(self, source: np.ndarray, extrema: list, offer_cost: float) -> float:
        gain_list = []
        gain_list = [source[extrema[j+1]] - source[extrema[j]] for j in range(0, len(extrema) - 1, 2)]
        gain_array = np.array(gain_list)
        gain = np.sum(gain_array) - len(extrema) * offer_cost
        return gain

    def calculate_gain_binary_annotation(self, source: np.ndarray, annotation: np.ndarray, extrema: list, offer_cost: float):

        

        return (np.where(annotation < -1, 0, annotation) * source).sum() - len(extrema) * offer_cost

    def _validate_array(self, source: np.ndarray, extrema: np.ndarray):
        if extrema[-1] > source.size:
            raise Exception(f'Max extrema address is larger than length of the subject array')