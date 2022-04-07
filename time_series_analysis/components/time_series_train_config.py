# coding: utf-8

from train.components import SigmaChanRNN
from typing import Any
import torch
import numpy as np

class TimeSeriesTrainConfig:
    """Abstract training model for time series analysis model"""
    def __init__(self) -> None:
        """Initialize training model in abstract items
        Args:
        Retuns:
        Attributes:
            self.n_len: int: data length of each item
            self.n_time: int: total number of data
            self.device: torch.device: training device
        """
        self.n_len = 256
        self.n_time = 10
        self.n_sample = self.n_len - self.n_time
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print("device: ", self.device, type(self.device))


    def load_sigma_chan_rnn(self) -> SigmaChanRNN:
        return SigmaChanRNN(256, 13)

