# coding: utf-8

from typing import Any
import json
from time_series_analysis.components import TimeSeriesNetworkConfig
from data_reader.data_structure.parameters import DataReader as DataReaderParameters
from data_reader.pipeline import DataReaderPipeline
from time_series_analysis.components.operators import obtain_todays_inference_parameter
import numpy as np
import torch


class TimeSeriesInferencePipeline:
    def __init__(self, parameters: DataReaderParameters) -> None:
        ### loading parameters
        if not isinstance(parameters, DataReaderParameters):
            raise TypeError(f"Input parameter for inference must be an instance of DataDeaderParameters")

        self.parameters = parameters

        ### initialize RNN inference
        self.inference_config = TimeSeriesNetworkConfig()
        self.inference_config.device = torch.device("cpu")

        self.model = self.load_model()

        ### initialize data reader pipeline
        self.data_reader = DataReaderPipeline(self.parameters)
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        
        data_tensor = self.data_reader.prepare_data_tensor()
        res = self.model(data_tensor)
        res_cpu = res.detach().numpy().copy()

        return res_cpu[0][0]

        

    def load_model(self) -> Any:
        ### compile model
        model = self.inference_config.compile_model()

        ### load model
        model = self.inference_config.load_model(model, "trained_model/20220413.pth")
        
        return model



        
    