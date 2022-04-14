# coding: utf-8

from time_series_analysis.components import TimeSeriesParameterGenerator


class TestTimeSeriesParameterGenerator:
    def test_obtain_todays_inference_parameter(self):
        generator = TimeSeriesParameterGenerator()


        parameter = generator.obtain_parameter_today(256)

        assert parameter["source"] == "fred"
        #assert parameter["end"] == "2022/04/10"
        #assert parameter["data_save_path"] == "data/fx/dexjpus_20220410.npy"
