# coding: utf-8

from pydantic import BaseModel, validator, root_validator

class DataReader(BaseModel):

    source: str
    source_candidates: list = ['yahoo_finance', 'fred']
    target: str
    target_candidates: list = ['DEXJPUS', 'EUR', 'CNY']
    end: str = ''
    duration: str = '1000'
    data_save_path: str = 'data/hoge.csv'
    
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

    @validator('end')
    def end_time(cls, v):
        if len(v.split('/')) != 3:
            raise ValueError(f'date format of \'end\' must be YY/mm/dd')

        return v