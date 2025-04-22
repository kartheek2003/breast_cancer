import os
import urllib.request 
import zipfile
from breast_cancer import logger
from breast_cancer.utils.common import get_size

from breast_cancer.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self,config : DataIngestionConfig ):
        self.config = config

    def download_file (self):
        logger.info(f"Starting download from {self.config.source_url}...")
        try:
            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)

            # Download the file
            urllib.request.urlretrieve(
                self.config.source_url,
                self.config.local_data_file
            )
            logger.info(f"Downloaded file to: {self.config.local_data_file}")
        except Exception as e:
            logger.error(f"Error during download: {e}")
            raise e
        return self.config.local_data_file