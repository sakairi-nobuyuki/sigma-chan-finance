# coding: utf-8

from time_series_analysis.components.operators.parameter_generator_today import obtain_todays_inference_parameter

class TimeSeriesParameterGenerator():
    def __init__(self) -> None:
        pass

    def obtain_parameter_today(self, duration: int):
        return obtain_todays_inference_parameter(duration)
        