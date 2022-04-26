# coding: utf-8

from data_reader.data_structure.parameters import DataReader as DataReaderParameters
from time_series_analysis.components.time_series_network_config import TimeSeriesNetworkConfig
from time_series_analysis.pipeline import TimeSeriesTrainPipeline, TimeSeriesInferencePipeline
from annotation.data_structure import DatasetParameters
import json
from fastapi import FastAPI

app = FastAPI()


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


def train_rnn_cli(job_id: str, parameters_path: str):
    with open(parameters_path) as f_in:
        parameters = json.load(f_in)
        parameters_str = json.dumps(parameters)
    train_rnn(job_id, parameters_str)



def infer_rnn_cli(job_id: str, parameters_path: str):
    with open(parameters_path) as f_in:
        parameters = json.load(f_in)
        parameters_str = json.dumps(parameters)
    infer_rnn(job_id, parameters_str)

@app.get("/")
async def infer_rnn():
#async def infer_rnn(job_id: str, parameters_str: str):    
    ### loading parameters
    ### Loading training parameters
    parameters_str = ""
    parameters_dict = json.loads(parameters_str)
    parameters = DataReaderParameters(**parameters_dict)
    inference = TimeSeriesInferencePipeline(parameters)

    ### inference
    print(inference())



#if __name__ == "__main__":
#    app()