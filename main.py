from breast_cancer import logger
import os

from breast_cancer.pipeline.stage01_data_ingestion import DataIngestionPipeline
from breast_cancer.pipeline.stage02_pre_processing import DataPreProessingPipeline

STAGE_NAME = "DATA INGESTION"
try :
        logger.info(f">>>>{STAGE_NAME} stage started<<<<")
        data_ingestion = DataIngestionPipeline()
        df= data_ingestion.main()
        logger.info(f">>>>{STAGE_NAME} COMPLETED <<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "PRE_PROCESSING"

try :
    logger.info(f">>>>{STAGE_NAME} STARTED<<<<")
    pre_processing = DataPreProessingPipeline(df)
    df_cleaned = pre_processing.main()

    logger.info(f"<<<<{STAGE_NAME} COMPLETED>>>>")

except Exception as e :
    logger.exception(e)
    raise e
