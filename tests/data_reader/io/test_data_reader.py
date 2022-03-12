# coding: utf-8

import os
import shutil
import pandas as pd

from data_reader.data_structure import parameters

from data_reader.data_structure.data_classes import DataReader as Input
from data_reader.data_structure.parameters import DataReader as Parameters

from data_reader.io import DataReader as Fx

class TestFredDataRead:
    def test_init(self, mock_exchange_rate_parameter):
        parameters = Parameters(**mock_exchange_rate_parameter)
        input = Input(parameters)

        parameters.source = 'fred'
        parameters.target = 'DEXJPUS'
        input = Input(parameters)

        print(vars(input))

        fred = Fx()
        
        fx_df = fred.read_data(input)
        
        assert isinstance(fx_df, pd.DataFrame)

    def test_file_save(self, mock_exchange_rate_parameter):
        parameters = Parameters(**mock_exchange_rate_parameter)
        parameters.source = 'fred'
        parameters.target = 'DEXJPUS'
        input = Input(parameters)

        fx = Fx()
        fx_df = fx.read_data(input)
        

        if not os.path.exists(os.path.dirname(input.data_save_path)):
            os.makedirs(os.path.dirname(input.data_save_path))
        else:
            os.remove(Path(input.data_save_path))

        fx.save_data_frame(fx_df, input.data_save_path)

        assert os.path.exists(input.data_save_path)

        shutil.rmtree(os.path.dirname(input.data_save_path))

    def test_dropped_date(self, mock_exchange_rate_parameter):
        parameters = Parameters(**mock_exchange_rate_parameter)
        parameters.source = 'fred'
        parameters.target = 'DEXJPUS'
        input = Input(parameters)

        fx = Fx()
        fx_df = fx.read_data(input)
        fx_df = fx.fill_dropped_date(fx_df)

        fx_df = fx.fill_dropped_date_value_by_fixed_value(fx_df, -1)
        fx_df = fx.fill_dropped_date_value_by_upwind_value(fx_df)

        print(fx_df.columns)
        print("values: ", fx_df[input.target].values)
