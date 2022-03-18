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

        return np.array(list(set(maxima[0].tolist() + minima[0].tolist())))

    def generage_extrema_combinations_set(self, extremas: np.ndarray):
        pass

    def generate_binary_comination(self, n: int):
        for i in range(2**n):

            yield np.array(list(bin(i)[2:].zfill(n))).astype(int)
        



    def obtain_extrema_combinations(self, extremas: np.ndarray) -> List[List[int]]:
        extremas_list = sorted(extremas.tolist())
        extrema_combinations_list = []
        
        for i in range(len(extremas_list)):
            #print(len(list(itertools.combinations(extremas_list, i))), i)
        
            #for combination in itertools.combinations(extremas_list, i):
            for combination in comb(extremas_list, i, exact=True):
                extrema_combinations_list.append(list(combination))
                print("length of extrema combination: ", len(extrema_combinations_list))

        extrema_combinations_list = [combination for combination in extrema_combinations_list if len(combination) > 2]

        return extrema_combinations_list

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
