# coding: utf-8


from typing import List
from numba import jit
import numpy as np
from scipy.signal import argrelmax, argrelmin
from skopt import gp_minimize
import datetime

from annotation.components import LossFunctions, LossFunctionsSingleArg


class ExtremaAnnotation:
    def __init__(self) -> None:
        self.loss = LossFunctions()
        


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
        print(f"total number of combinations: {2**extremas_length}, {extremas}")
        
        for i in range(2**extremas_length):
            
            selected_array = self.obtain_binary_combination(i, extremas_length) * extremas
            yield selected_array[selected_array.nonzero()]

    def obtain_extrema_combination(self, extremas: np.ndarray, i: int, n: int):
        selected_array = self.obtain_binary_combination(i, n) * extremas
        return selected_array[selected_array.nonzero()]

    
    def obtain_extrema_combinations(self, source: np.ndarray, extremas: np.ndarray, offer_cost: float):
        extremas_length = extremas.size
        combination_generator = self.extrema_combinations_generator(extremas)
        loss = 0.0
        start = datetime.datetime.now()
        minor_extrema_tmp = np.array([0])
        for i in range(2**extremas_length):
            minor_extrema = combination_generator.__next__()
            loss_tmp = self.loss.calculate_gain(source, minor_extrema, offer_cost)
            
            if loss_tmp > loss:
                loss = loss_tmp
                minor_extrema_tmp = minor_extrema
                print(f"  in {i} th combination evaluation, loss = {loss_tmp}, combination_minor = {minor_extrema}, timedelta = {datetime.datetime.now() - start}")
        return minor_extrema_tmp


    def obtain_extrema_best_combination_by_baysian(self, source: np.ndarray, extremas: np.ndarray, offer_cost: float):
        
        pass

class MoreBetterPattern:
    def __init__(self, loss: LossFunctionsSingleArg) -> None:
        self.loss = loss

    def obtain_extrema_combinations(self, source: np.ndarray, extremas: np.ndarray, offer_cost: float):
        res = gp_minimize(self.loss.calculate_gain, [])
        
    

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
