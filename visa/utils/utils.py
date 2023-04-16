import os , sys
from visa.logger import logging
from visa.exception import CustomException
import yaml

def read_yaml(filepath:str)-> str:
    try:
        with open(filepath , 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e , sys)
    
