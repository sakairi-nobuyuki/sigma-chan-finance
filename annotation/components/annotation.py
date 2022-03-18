# coding: utf-8

from typing import List
import numpy as np
from scipy.signal import argrelmax, argrelmin
from scipy.special import comb
import itertools

class ExtremaAnnotation:
#    def __init__(self, source: np.ndarray) -> None:
#        self.source = source

    def __init__(self) -> None:
        self._binary_combination_list = []
        pass


    def __call__(self, source) -> np.ndarray:
        return self.obtain_extrema_combinations(self.obtain_maxima_minima(source))


    def obtain_maxima_minima(self, source: np.ndarray) -> np.ndarray:
        maxima = argrelmax(source)
        minima = argrelmin(source)
        
        if len(maxima) == 0 or len(minima) == 0:
            raise ValueError('Size of annotation source is too small so that no obvious zero gradient point was found.')

        return np.array(sorted(list(set(maxima[0].tolist() + minima[0].tolist()))))

    def generage_extrema_combinations_set(self, extremas: np.ndarray):
        pass

    def binary_comination_generator(self, n: int):
        for i in range(2**n):
            yield np.array(list(bin(i)[2:].zfill(n))).astype(int)
        
    def obtain_binary_combination(self, i: int, n: int):
        return np.array(list(bin(i)[2:].zfill(n))).astype(int)


    def extrema_combinations_generator(self, extremas: np.ndarray) -> List[List[int]]:
        extremas_length = extremas.size
        for i in range(2**extremas_length):
            selected_array = self.obtain_binary_combination(i, extremas_length) * extremas
            yield selected_array[selected_array.nonzero()]


class PutCallAnnotation:
    def __init__(self) -> None:
        pass

    def __call__(self, source: np.ndarray, extrema: list) -> np.ndarray:
        return self.annotate_binary(source, extrema)

    def annotate_binary(self, source: np.ndarray, extrema: list) -> np.ndarray:
        annotated = np.zeros(source.size)
        for j in range(0, len(extrema) - 1, 2):
            annotated[extrema[j]: extrema[j + 1]] = 1
        annotated[:1] = -1
        annotated[-1:] = -1

        return annotated
