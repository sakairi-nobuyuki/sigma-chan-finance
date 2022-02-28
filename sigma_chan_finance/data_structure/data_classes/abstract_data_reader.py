# coding: utf-8

from typing import Any, List
from abc import ABCMeta, abstractmethod

class AbstractDataReader(metaclass=ABCMeta):
    source: str
    target: str
    start: Any
    end: Any
    duration: Any
    values: Any

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def validate_end(self) -> Any:
        pass

        