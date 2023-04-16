import os
import sys
import logging
from datetime import datetime


def current_datetime_stamp()->str:
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


CURRENT_TIME_STAMP = current_datetime_stamp()

ROOT_DIR = os.getcwd()
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR , CONFIG_DIR , CONFIG_FILE_NAME)

# Data Ingestion related variable 

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATASET_DOWNLOAD_URL = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
INGESTED_TRAIN_DIR_KEY = "ingested_train_dir"
INGESTED_TEST_DIR_KEY = "ingested_test_dir"
INGESTED_DIR_KEY = "ingested_dir"
DATA_INGESTION_ARTIFACTS_DIR = "data_ingestion"