# coding: utf-8

from time_series_analysis.components import SigmaChanRNN
from typing import Any
import torch
import numpy as np

class TimeSeriesNetworkConfig:
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

    def compile_model(self) -> Any:
        """Configure and compile the model structure according to the setting parameter
        
        Return: 
            model: torch.nn: model"""

        model = self.load_sigma_chan_rnn().to(self.device)

        return model


    def load_model(self, model: Any, model_path: str, gpu_flag: bool = False) -> Any:
        if gpu_flag:
            model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
        else:
            model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))

        return model

    def save_model(self, model_path: str, model: Any, gpu_flag: bool = False) -> None: 
        if "pth" not in model_path.split(".")[-1]:
            model_path = model_path + ".pth"

        if gpu_flag:
            torch.save(model.state_dict(), model_path)
        else:
            torch.save(model.to("cpu").state_dict(), model_path)