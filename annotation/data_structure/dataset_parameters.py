# coding: utf-8

import typing


from typing import Optional
from pydantic import BaseModel


class DatasetDirectoryParameters(BaseModel):
    train: str = "dataset/annotation/train"
    validation: Optional[str] = "dataset/annotation/validation"
    test: Optional[str] = "dataset/annotation/test"

class DatasetCreationParameters(BaseModel):
    length: int = 256
    offer_cost: float = 0.0

class DatasetParameters(BaseModel):
    root_dir: str = None
    source_dir: str = "data/"
    target_dir: DatasetDirectoryParameters
    dataset_spec: DatasetCreationParameters
    
