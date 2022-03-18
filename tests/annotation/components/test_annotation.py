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
        maxima_minima = annotation.obtain_maxima_minima(source)
        print(type(maxima_minima))
        #print(annotation.obtain_extrema_combinations(maxima_minima))




@pytest.mark.itertools
class TestIterator:
    def test_binary_combination_generator(self):
        extrema_annotation = ExtremaAnnotation()
        binary_combination_generator = extrema_annotation.binary_comination_generator(5)
        
        print(type(binary_combination_generator.__next__()))

        np.testing.assert_array_equal(binary_combination_generator.__next__(), np.array([0, 0, 0, 0, 1]))
        
    def test_binary_combination(self):
        extrema_annotation = ExtremaAnnotation()
        np.testing.assert_array_equal(extrema_annotation.obtain_binary_combination(1, 5), np.array([0, 0, 0, 0, 1]))

    def test_extrema_combinations_generator(self):
        extrema_annotation = ExtremaAnnotation()
        source = np.array([random.random() for i in range(5)])
        extrema = extrema_annotation.obtain_maxima_minima(source)
        binary_combination_generator = extrema_annotation.extrema_combinations_generator(extrema)
        print(source, extrema)
        print(binary_combination_generator.__next__())
        print(binary_combination_generator.__next__())
        print(binary_combination_generator.__next__())
        print(binary_combination_generator.__next__())