# coding: utf-8

from annotation.io import DataLoader, data_loader
import pytest


class TestDataLoader:
    def test_init(self):
        data_loader = DataLoader()

        print(data_loader.working_dir)
        print(data_loader.data_dir)
        print(data_loader.data_file_list)

    def test_init(self):
        data_loader = DataLoader()

        array_list = data_loader.load_data()

        assert len(array_list) > 0
        assert array_list[0].ndim > 0