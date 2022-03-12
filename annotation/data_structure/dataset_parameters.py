# coding: utf-8

import typing


from typing import Optional, List
from pydantic import BaseModel, validator


class DatasetDirectoryParameters(BaseModel):
    train: str = "dataset/annotation/train"
    validation: Optional[str] = "dataset/annotation/validation"
    test: Optional[str] = "dataset/annotation/test"

class DatasetCreationParameters(BaseModel):
    length: int = 256
    number_of_data: int = 100
    offer_cost: float = 0.0

class DatasetParameters(BaseModel):
    root_dir: str = None
    source_dir: str = "data/"
    target_dir: DatasetDirectoryParameters
    dataset_spec: DatasetCreationParameters
    distribute_ratio: List[float] = [0.7, 0.2, 0.1]
    
    @validator("distribute_ratio")
    def _validate_distribution_ratio(cls, v):
        if sum(list) < 1.0:
            print(f'Warning: sum of the distribution ratio of [train, validation, test] is less than 1.0. Modified to {v}')
            v[1] = 1.0 - v[0] - v[2]
            return v
        if sum(list) > 1.0:
            raise Exception(f'Warning: sum of the distribution ratio of [train, validation, test] is larger than 1.0.')


