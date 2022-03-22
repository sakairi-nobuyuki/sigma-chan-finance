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

    def test_create_representative_set(self):
        labels = np.array([0, 0, 1, 1, 2, 2])
        src = np.array([0, 1, 2, 3, 4, 5])

        knn2 = TwoDimKNN()
        res = knn2.create_representative_set(src, labels)
        print("result of representative: ", res)



