# coding: utf-8

import numpy as np
from numba import jit

from annotation.components import ExtremaAnnotation

class LossFunctions:
    def __init__(self) -> None:
        pass
        
    def __call__(self, source: np.ndarray, extrema: np.ndarray, offer_cost: float) -> float:
        return self.calculate_gain(source, extrema, offer_cost)

   # @jit(nopython=True)
    def calculate_gain(self, source: np.ndarray, extrema: list, offer_cost: float) -> float:
        gain_list = []
        gain_list = [source[extrema[j+1]] - source[extrema[j]] for j in range(0, len(extrema) - 1, 2)]
        gain_array = np.array(gain_list)
        gain = np.sum(gain_array) - len(gain_list) * offer_cost
        return gain


    def calculate_gain_binary_annotation(self, source: np.ndarray, annotation: np.ndarray, offer_cost: float):
        mark = self.obtain_delta(annotation)
        print(self.obtain_up_down(annotation))
        return np.sum(mark.astype(float) * source) - self.obtain_up_down(annotation) * offer_cost

    def obtain_up_down(self, source: np.ndarray) -> np.array:
        delta_positive = source[1:] - source[:-1]
        delta_positive = np.where(delta_positive > 0, delta_positive, 0)
        
        return np.sum(delta_positive)

    def obtain_delta(self, source: np.ndarray) -> np.ndarray:
        source_add = np.append(0, source)
        source_add = np.append(source_add, 0)

        delta_negative = source_add[: -1] - source_add[1 :]
        delta_negative = np.append(delta_negative[0], delta_negative)
        delta_negative = np.where(delta_negative < 0, delta_negative, 0)

        delta_positive = source_add[: -1] - source_add[1 :]
        delta_positive = np.append(delta_positive, delta_positive[-1])
        delta_positive = np.where(delta_positive > 0, delta_positive, 0)

        delta = delta_positive + delta_negative

        delta = delta[1: -1]

        return delta

    def _validate_array(self, source: np.ndarray, extrema: np.ndarray):
        if extrema[-1] > source.size:
            raise Exception(f'Max extrema address is larger than length of the subject array')

class LossFunctionsSingleArg:
    def __init__(self, source: np.ndarray, extremas: np.ndarray, offer_cost: float, extrema_annotation: ExtremaAnnotation) -> None:
        """Loss function for Bayes optimization by skopt.
        Args:
            source: np.ndarray: Trading values in series
            extremas: np.ndarray: Args of extremas of trading values"""

        self.source = source
        self.extremas = extremas
        self.offer_cost = offer_cost

        if not isinstance(extrema_annotation, ExtremaAnnotation):
            raise TypeError(f"On initializing 1 arg loss function, annotation instance is not that of ExtremaAnnotation")
        self.extrema_annotation = extrema_annotation


    def calculate_gain(self, i_eval: int) -> float:
        #source: np.ndarray, extrema: list, offer_cost: float) -> float:
        extrema = self.extrema_annotation.obtain_extrema_combination(self.extremas, i_eval, self.extremas.size)
        gain_list = []
        gain_list = [self.source[extrema[j+1]] - self.source[extrema[j]] for j in range(0, len(extrema) - 1, 2)]
        gain_array = np.array(gain_list)
        gain = np.sum(gain_array) - len(gain_list) * self.offer_cost
        return gain


    def calculate_gain(self, i_eval: int) -> float:
        return super().calculate_gain(self.source[i_eval], self.extrema[i_eval], self.offer_cost)