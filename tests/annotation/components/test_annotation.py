# coding: utf-8


from email.generator import Generator
from annotation.components import ExtremaAnnotation
import numpy as np
import random
import pytest
import itertools

class TestAnnotation:
    def test_init(self, mock_one_dim_ndarray: np.ndarray):
        #annotation = ExtremaAnnotation(mock_one_dim_ndarray)
        annotation = ExtremaAnnotation()
        
        assert isinstance(annotation, ExtremaAnnotation)
        assert len(list(annotation.obtain_maxima_minima(mock_one_dim_ndarray))) > 0

    def test_peaks(self):
        source = np.array([random.random() for i in range(10)])

        print(source)

        annotation = ExtremaAnnotation()

        print(annotation.obtain_maxima_minima(source))
        print(annotation.obtain_extrema_combinations(annotation.obtain_maxima_minima(source)))

def select(i: int, target_list: list, res_list: list):
    if i == len(target_list):
        print("in select function, ", i, target_list, res_list)
        res_list.append(target_list)
        

        return res_list
        #return res_list
        #return target_list
        #yield target_list
    else:
        select(i + 1, target_list, res_list)
        target_list[i] = 1
        
        select(i + 1, target_list, res_list)
        target_list[i] = 0

    
def recursive_comb(n: int):
    target = [0] * n
    res_list = []
    select(0, target, res_list)

    print("in recursive comb", target)

    return res_list



@pytest.mark.itertools
class TestIterator:
    def test_iterator_generator(self):
        target_list = [1, 2, 3]
        gen = itertools.combinations(target_list, 2)
        assert gen.__next__() == (1, 2)

    def test_iterator_recursive(self):
        target_list = [1, 2, 3, 4]
        res_list = []
        for i in range(len(target_list)):
            print(i)
            for j in range(i+1, len(target_list)):
                print(j)
                res_list.append([i, j])

                print([i, j])

    def test_iterator_recursive_external(self):
        target_list = [1, 2, 3, 4]
        res_list = []

        print("res_list", recursive_comb(5))

    def test_binary_combination_generator(self):
        extrema_annotation = ExtremaAnnotation()
        binary_combination_generator = extrema_annotation.generate_binary_comination(5)
        
        print(type(binary_combination_generator.__next__()))

        np.testing.assert_array_equal(binary_combination_generator.__next__(), np.array([0, 0, 0, 0, 1]))
        
        

