from breast_cancer.entity.config_entity import PreProcessing
from breast_cancer import logger
import os

class DataPreProcess :
    def __init__(self,config:PreProcessing):
        self.config = config
    
    def get_preprocess_data(self,df) :
        try:
            df_cleaned = df.drop(self.config.drop_columns,axis=self.config.axis)
            logger.info("data frame preprocessing")
            df_cleaned.to_csv(os.path.join(self.config.df_pre_dir,"df_clean.csv"),index=False)
            logger.info(f"df_cleaned saved at {self.config.df_pre_dir}")
            return df_cleaned
        except Exception as e:
            logger.info("unable to preprocess")
            raise e
        