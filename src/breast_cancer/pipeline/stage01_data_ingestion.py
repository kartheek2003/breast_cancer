from breast_cancer.config.configuration import  ConfigurationManager
from breast_cancer.components.data_ingestion import DataIngestion
from breast_cancer import logger
import pandas as pd
from pathlib import Path

STAGE_NAME = "DATA INGESTION"

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config= data_ingestion_config)
        csv_path =  Path(data_ingestion.download_file())
        df = pd.read_csv(csv_path)

        return df

if __name__ == "__main__":
    try :
        logger.info(f">>>>{STAGE_NAME} stage started<<<<")
        obj = DataIngestionPipeline()
        df= obj.main()
        logger.info(f">>>>{STAGE_NAME} COMPLETED <<<<")

    except Exception as e:
        logger.exception(e)
        raise e