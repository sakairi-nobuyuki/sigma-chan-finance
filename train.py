# coding: utf-8

from train.pipeline import TimeSeriesTrainPipeline
from annotation.data_structure import DatasetParameters
import json

def train_rnn(job_id: str, parameters_str: str):
    ### Loading training parameters
    parameters_dict = json.loads(parameters_str)
    dataset_parameters = DatasetParameters(**parameters_dict)

    ### Initialize training pipeline
    train_pipeline = TimeSeriesTrainPipeline()
    
    ### Preparation of training dataset 
    train_loader =  train_pipeline.create_train_dataset(dataset_parameters)

    ### Train
    train_pipeline.train_model(1000, train_loader)
    


if __name__ == "__main__":
    with open("data/parameters/fx_usd_220313.json") as f_in:
        parameters = json.load(f_in)
        parameters_str = json.dumps(parameters)
    train_rnn("test_01", parameters_str)