# coding: utf-8



from sigma_chan_finance.data_structure.parameters import DataReader as Parameters
from sigma_chan_finance.data_structure.data_classes import DataReader as DataClass
from sigma_chan_finance.io import DataReader as InputOutput
from sigma_chan_finance.pipeline import DataReader

import json
import argparse
import pprint

def read_data(job_id: str, parameters_str: str) -> None:
    parameters_dict = json.loads(parameters_str)
    parameters = Parameters(**parameters_dict)
    print("parameters: ")
    pprint.pprint(parameters)
    data_class = DataClass(parameters)
    
    io = InputOutput()

    data_reader = DataReader()
    data_reader(io, data_class)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('job_id')
    parser.add_argument('parameters_path')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = get_args()

    with open(args.parameters_path, 'r') as f_in:
        parameters_dict = json.load(f_in)
    parameters_str = json.dumps(parameters_dict)

    read_data(args.job_id, parameters_str)