# coding: utf-8

from typing import Any
from time_series_analysis.components import TimeSeriesNetworkConfig
from annotation.pipeline import RnnDatasetPreparation
from annotation.data_structure import DatasetParameters
from data_reader.data_structure.parameters import DataReader as DataReaderParameters
import torch


class TimeSeriesInferencePipeline:
    def __init__(self, parameters: DataReaderParameters) -> None:
        if not isinstance(parameters, DataReaderParameters):
            raise TypeError(f"Input parameter for inference must be an instance of DataDeaderParameters")
        
        self.inference_config = TimeSeriesNetworkConfig()