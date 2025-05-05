from breast_cancer.config.configuration import ConfigurationManager
from breast_cancer.components.pre_processing import DataPreProcess
from breast_cancer import logger
import pandas as pd
from pathlib import Path

STAGE_NAME = "PRE_PROCESSING"

class DataPreProessingPipeline:
    def __init__(self,df):
        self.df = df
    def main(self):
        config = ConfigurationManager()
        pre_processing_config = config.preprocessing()
        data_pre_process = DataPreProcess(config=pre_processing_config)
        df_cleaned = data_pre_process.get_preprocess_data(df=self.df)

        return df_cleaned
        
if __name__ == "__main__":
    try :
        logger.info(f">>>>{STAGE_NAME} STARTED<<<<")
        obj = DataPreProessingPipeline()
        df_cleaned = obj.main()
        logger.info(f"<<<<{STAGE_NAME} COMPLETED>>>>")

    except Exception as e :
        logger.exception(e)
        raise e
