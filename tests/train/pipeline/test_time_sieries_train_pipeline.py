# coding: utf-8


from train.pipeline import TimeSeriesTrainPipeline
from train.components import SigmaChanRNN

class TestTimeSeriesTrainPipeline:
    def test_init(self):
        train_pipeline = TimeSeriesTrainPipeline()

        assert isinstance(train_pipeline, TimeSeriesTrainPipeline)
        assert isinstance(train_pipeline.model, SigmaChanRNN)