# coding: utf-8

from data_reader.data_structure.parameters import DataReader as Parameters
from data_reader.data_structure.data_classes import DataReader as DataClass
from data_reader.io import DataReader as InputOutput
from data_reader.pipeline import DataReader

import json
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
    
    return data_reader(io, data_class)


