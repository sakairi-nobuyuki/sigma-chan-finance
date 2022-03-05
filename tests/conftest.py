# coding: utf-8

import pytest
import numpy as np

@pytest.fixture(scope='function')
def mock_exchange_rate_parameter():
    parameter_dict = {
        'source': 'yahoo_finance',
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