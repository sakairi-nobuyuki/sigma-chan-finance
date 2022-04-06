# coding: utf-8

import os
import numpy as np
from train.pipeline import TimeSeriesTrainPipeline
from train.components import SigmaChanRNN


class TestTimeSeriesTrainPipeline:
    def test_init(self):
        train_pipeline = TimeSeriesTrainPipeline()

        assert isinstance(train_pipeline, TimeSeriesTrainPipeline)
        assert isinstance(train_pipeline.model, SigmaChanRNN)

    def test_save_load_model(self, mock_dataset_parameters):
#        parameters = DatasetParameters(**mock_dataset_parameters)
        time_series_train_pipeline = TimeSeriesTrainPipeline()

        model_path = "test_model.pth"
        if os.path.exists(model_path):
            os.remove(model_path)
        time_series_train_pipeline.save_model(model_path)

        assert os.path.exists(model_path)

        time_series_train_pipeline_2 = TimeSeriesTrainPipeline()

        time_series_train_pipeline_2.load_model(model_path)

        weight = time_series_train_pipeline.model.network.weight_ih_l0.to("cpu").detach().numpy().copy()
        weight2 = time_series_train_pipeline_2.model.network.weight_ih_l0.to("cpu").detach().numpy().copy()

        np.testing.assert_array_equal(weight, weight2)

        if os.path.exists(model_path):
            os.remove(model_path)

 
