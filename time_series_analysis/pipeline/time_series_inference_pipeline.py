# coding: utf-8

from typing import Any
from time_series_analysis.components import TimeSeriesNetworkConfig
from annotation.pipeline import RnnDatasetPreparation
from annotation.data_structure import DatasetParameters
import torch


class TimeSeriesInferencePipeline:
    def __init__(self) -> None:
        self.inference_config = TimeSeriesNetworkConfig()