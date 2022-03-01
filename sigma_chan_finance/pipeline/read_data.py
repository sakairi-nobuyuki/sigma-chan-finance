# coding: utf-8


from sigma_chan_finance.data_structure.parameters import DataReader as Parameters
from sigma_chan_finance.data_structure.data_classes import DataReader as DataClass
from sigma_chan_finance.io import DataReader as InputOutput
from sigma_chan_finance.pipeline import DataReader

import json
import argparse

def read_data(job_id: str, parameters_str: str) -> None:
    parameters = Parameters(**json.loads(parameters_str))
    data_class = DataClass(parameters)
    io = InputOutput()

    data_reader = DataReader()
    data_reader(io, data_class)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add('job_id')
    parser.add('parameters_path')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = get_args()

    with open(args.parameters_path, 'r') as f_in:
        parameters_dict = json.load(f_in)
    parameters_str = json.loads(parameters_dict)

    read_data(args.job_id, parameters_str)