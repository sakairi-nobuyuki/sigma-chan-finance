# coding: utf-8

from abc import ABCMeta, abstractmethod
from annotation.data_structure import AbstractData

class AbstractDataFactory(metaclass=ABCMeta):

    
    def create(self, data: AbstractData):
        pass

    def create_product(self, data: AbstractData):
        pass


