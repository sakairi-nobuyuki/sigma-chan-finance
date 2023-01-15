# coding: utf-8



from data_reader.data_structure.parameters import DataReader as Parameters
from data_reader.data_structure.data_classes import DataReader as DataClass
from data_reader.io import DataReader as InputOutput
from data_reader.pipeline import DataReader

import json
import argparse
import pprint
import typer

app = typer.Typer()


def read_data(job_id: str, parameters_str: str) -> None:
    parameters_dict = json.loads(parameters_str)
    parameters = Parameters(**parameters_dict)
    print("parameters: ")
    pprint.pprint(parameters)
    data_class = DataClass(parameters)

    io = InputOutput()

    data_reader = DataReader()
    

    io.save_values_as_ndarray(data_reader(io, data_class), data_class.data_save_path)


@app.command()
def read_data_cli(job_id: str, parameters_path: str):
    with open(parameters_path, 'r') as f_in:
        parameters_dict = json.load(f_in)
    parameters_str = json.dumps(parameters_dict)

    read_data(job_id, parameters_str)

if __name__ == '__main__':
    app()
