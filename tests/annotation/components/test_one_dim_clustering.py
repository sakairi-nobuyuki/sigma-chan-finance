# coding: utf-8

from annotation.components import OneDimKNN


class TestOneDimKnn:
    def test_init(self, mock_ndarray_for_cluster):
        model = OneDimKNN()
        
        labels = model.fit(mock_ndarray_for_cluster, 3)
        print(type(labels))

        print(labels)