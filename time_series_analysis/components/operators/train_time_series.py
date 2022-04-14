# coding: utf-8

from components.operators import SigmaChanRNN
from typing import Any
import torch
import numpy as np

class TimeSeriesTrain:
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

        ### compile model
        self.model = self.compile_model()
        self.loss = torch.nn.L1Loss()
        self.optimizer = torch.optim.SGD(self.model.parameters(), lr=0.01)


    def compile_model(self) -> Any:
        model = self.load_sigma_chan_rnn()

        return model
        

    def load_sigma_chan_rnn(self) -> SigmaChanRNN:
        return SigmaChanRNN(256, 13)


    def train_model(self, n_epochs: int):

        for i in range(n_epochs):
            pass