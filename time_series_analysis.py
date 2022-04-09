# coding: utf-8

from time_series_analysis.components.time_series_network_config import TimeSeriesNetworkConfig
from time_series_analysis.pipeline import TimeSeriesTrainPipeline
from annotation.data_structure import DatasetParameters
import json
import typer

app = typer.Typer()


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

@app.command()    
def train_rnn_cli(job_id: str, parameters_path: str):
    with open(parameters_path) as f_in:
        parameters = json.load(f_in)
        parameters_str = json.dumps(parameters)
    train_rnn(job_id, parameters_str)


def infer_rnn(job_id: str, parameters_str: str):
    ### loading parameters


    ### generate data load parameters


    ### load data


    ### initialize RNN inference


    ### inference


    ### postprocess

    pass

if __name__ == "__main__":
    app()