# coding: utf-8

from typing import Any
from time_series_analysis.components import TimeSeriesNetworkConfig
from annotation.pipeline import RnnDatasetPreparation
from annotation.data_structure import DatasetParameters
from data_reader.data_structure.parameters import DataReader as DataReaderParameters
from data_reader.pipeline import DataReaderPipeline
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

    def load_model(self) -> Any:
        ### compile model
        model = self.inference_config.compile_model()

        ### load model
        model = self.inference_config.load_model(model, "trained_model/20220413.pth")
        
        return model

    
        