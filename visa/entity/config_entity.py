from collections import namedtuple



DataIngestionConfig = namedtuple("data_ingestion_config" , 
    ['dataset_download_url' , 'raw_data_dir'  , 'ingested_train_dir' , 'ingested_test_dir'])


