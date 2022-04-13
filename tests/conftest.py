# coding: utf-8

from annotation import data_structure
from annotation.data_structure import dataset_parameters
import pytest
import numpy as np

@pytest.fixture(scope='function')
def mock_exchange_rate_parameter():
    parameter_dict = {
        'source': 'fred',
        'target': 'DEXJPUS',
        'end': '2022/02/27',
        'duration': '100'
    }
    return parameter_dict


@pytest.fixture(scope='function')
def mock_one_dim_ndarray():
    return np.array([-1, 0, 1, -2, -1])

@pytest.fixture(scope='function')
def mock_one_dim_oscillating_ndarray():
    return np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])    


@pytest.fixture(scope="function")
def mock_dataset_creation_parameters():
    dataset_creation_dict = {
        "length": 256,
        "offer_cost": 2.0,
        "number_of_data": 10
    }

    return dataset_creation_dict


@pytest.fixture(scope="function")
def mock_dataset_directory_parameters():
    dataset_directory_parameters = {
        "train": "data/annotation/train",
        "validation": "data/annotation/validataion",
        "test": "data/annotation/test"
    }
    return dataset_directory_parameters

@pytest.fixture(scope="function")
def mock_dataset_parameters():
    dataset_parameters = {
        "root_dir": "",
        "source_dir": "data/",
        "target_dir": {
            "train": "data/annotation/train",
            "validation": "data/annotation/validataion",
            "test": "data/annotation/test"
        },
        "dataset_spec": {
            "length": 256,
            "offer_cost": 2.0            
        }
    }
    return dataset_parameters