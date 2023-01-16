# config: utf-8

from annotation.data_structure import DatasetParameters
from abc import ABCMeta, abstractmethod
import random
from typing import List, Any
import numpy as np
import dataclasses


@dataclasses.dataclass
class AnnotationDataClass:
    source: List[np.ndarray]
    annotated: List[np.ndarray]

@dataclasses.dataclass
class AbstractData(metaclass=ABCMeta):
    source: np.ndarray
    annotation: np.ndarray

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.__init__()

class BinaryData(AbstractData):
    res: int
    loss: float

    def __init__(self, source: np.ndarray, annotation: np.ndarray, res: int, loss: float) -> None:
        self.source = source
        self.annotation = annotation
        self.res = res
        self.loss = loss

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)

@dataclasses.dataclass
class AbstractDataset(metaclass=ABCMeta):
    train: List[AbstractData] = dataclasses.field(default_factory=list)
    validation: List[AbstractData] = dataclasses.field(default_factory=list)
    test: List[AbstractData] = dataclasses.field(default_factory=list)

    @abstractmethod
    def append_random(self, data: AbstractData, dataset_parameters: DatasetParameters):
        self.validate_data(data)

        rand = random.random()
        if rand < dataset_parameters.distribute_ratio[0]:
            self.train.append(data)
        elif sum(dataset_parameters.distribute_ratio) < rand: 
            self.test.append(data)
        else:
            self.validation.append(data)

    @abstractmethod
    def validate_data(self, data: AbstractData):
        if not isinstance(data, AbstractData):
            raise TypeError(f"Type of the data is not correct: {type(data)}")


class BinaryDataset(AbstractDataset):

    def append_random(self, data: BinaryData, dataset_parameters: DatasetParameters):
        return super().append_random(data, dataset_parameters)
    def validate_data(self, data: BinaryData):
        return super().validate_data(data)

