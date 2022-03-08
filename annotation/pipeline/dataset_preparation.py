# coding: utf-8


from annotation.data_structure import DatasetParameters
from annotation.io import DataLoader

class DatasetPreparation:
    def __init__(self, parameters: DatasetParameters) -> None:
        if not isinstance(parameters, DatasetParameters):
            raise Exception(f"Instance of dataset parameters are not valid")
        
        self.parameters = parameters
        

    
        
        




