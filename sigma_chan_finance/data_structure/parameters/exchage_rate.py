# coding: utf-8

from pydantic import BaseModel, validator, root_validator
import dataclasses
import numpy as np
import datetime

class ExchangeRate(BaseModel):

    source: str
    source_candidates: list = ['yahoo_finance']
    target: str
    target_candidates: list = ['USD', 'EUR', 'CNY']
    end: str 
    duration: str


    
    @root_validator
    def source_type(cls, values):
        if values['source'] not in values['source_candidates']:
            raise ValueError('{} must be in {}'.format(values['source'], values['source_candidates']))
        return values

    @root_validator
    def target_name(cls, values):
        if values['target'] not in values['target_candidates']:
            raise ValueError('{} must be in {}'.format(values['target'], values['target_candidates']))
        return values

