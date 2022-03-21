# coding: utf-8

from annotation.components import TwoDimKNN
import numpy as np

class TestTwoDimKnn:
    def test_init(self, mock_ndarray_for_cluster):
        model = TwoDimKNN()

        array_pos = (mock_ndarray_for_cluster * 100).astype(int)

        labels = model.fit(mock_ndarray_for_cluster, array_pos, 3)
        print(type(labels))

        print(labels)