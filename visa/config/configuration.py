import os , sys
from visa.config import *
from visa.logger import logging
from visa.exception import CustomException
from visa.entity.config_entity import DataIngestionConfig
from visa.utils.utils import read_yaml


class Configuration:
    def __init__(self , 
                 config_file_path:str =CONFIG_FILE_PATH,
                 current_timestamp:str= CURRENT_TIME_STAMP) -> None:
        try:
            self.config_file_path = read_yaml(filepath=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_timestamp
        except Exception as e:
            raise CustomException(e , sys)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            artifacts_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifacts_dir = os.path.join(artifacts_dir , DATA_INGESTION_ARTIFACTS_DIR,
                                                        self.time_stamp)
            data_ingestion_info = self.config_file_path[DATA_INGESTION_CONFIG_KEY]
            dataset_download_url = self.config_file_path[DATASET_DOWNLOAD_URL]

            raw_data_dir = os.path.join(data_ingestion_artifacts_dir , 
                                        data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])
            
            ingested_data_dir = os.path.join(data_ingestion_artifacts_dir , 
                                        data_ingestion_info[INGESTED_DIR_KEY])
            
            ingested_train_dir = os.path.join(ingested_data_dir ,
            data_ingestion_info[INGESTED_TRAIN_DIR_KEY])
            
            ingested_test_dir = os.path.join(ingested_data_dir ,
            data_ingestion_info[INGESTED_TEST_DIR_KEY])

            data_ingestion_config = DataIngestionConfig(dataset_download_url=dataset_download_url , 
                                                        raw_data_dir=raw_data_dir ,
                                                        ingested_train_dir=ingested_train_dir,
                                                        ingested_test_dir=ingested_test_dir)
            
            return data_ingestion_config

        except Exception as e:
            raise CustomException(e , sys)
        

