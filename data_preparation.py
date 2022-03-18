# coding: utf-8


from annotation.pipeline import DatasetPreparation
import json


def obtain_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('job_id')
    parser.add_argument('parameters_path')

    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = obtain_args()
    print(args.job_id, args.parameters_path)
    with open(args.parameters_path) as f_in:
        parameters = json.load(f_in)
    parameters_str = json.dumps(parameters)
    print(args.job_id, parameters_str)
    dataset_prepare = DatasetPreparation(args.job_id, parameters_str)
    dataset_prepare.dataset_preparation()