# coding: utf-8

from data_reader.data_structure.parameters import DataReader as Parameters
from data_structure.data_classes import DataReader as DataClass
from io import DataReader as InputOutput
from pipeline import DataReader

import json
import argparse
import typer

app = typer.Typer()

@app.command()
def read_data(job_id: str, parameters_str: str) -> None:
    """Get data from somewhere.
    Data save to a path defined in the parameter
    
    Args:
        job_id: str: job_id
        parameters_str: str: parameters for getting data in str
    """
    parameters = Parameters(**json.loads(parameters_str))
    data_class = DataClass(parameters)
    io = InputOutput()

    data_reader = DataReader()
    data_reader(io, data_class)


@app.command()
def read_data_cli(job_id: str, parameters_path: str) -> None:
    with open(parameters_path, 'r') as f_in:
        parameters_dict = json.load(f_in)
    parameters_str = json.loads(parameters_dict)

    read_data(job_id, parameters_str)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add('job_id')
    parser.add('parameters_path')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    app()

    
    #args = get_args()

    #with open(args.parameters_path, 'r') as f_in:
    #    parameters_dict = json.load(f_in)
    #parameters_str = json.loads(parameters_dict)

    #read_data(args.job_id, parameters_str)