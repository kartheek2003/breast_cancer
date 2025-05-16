import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))
from breast_cancer.constants import  *

from breast_cancer.utils.common import read_yaml , create_directories

from breast_cancer.entity.config_entity import DataIngestionConfig , PreProcessing , EDAconfig , DataTransform , ModelBuilding , Prediction

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH, 
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_url,
            local_data_file= config.local_data_file,
            
        )

        return data_ingestion_config
    
    def preprocessing(self) -> PreProcessing:
        params = self.params.preprocessing
        config = self.config.preprocessing
        
        create_directories([config.df_pre_dir])
        pre_processing = PreProcessing(df_pre_dir=config.df_pre_dir,drop_columns=params.drop_columns,axis = params.axis)
        
        return pre_processing


    def EDA_configuration(self) -> EDAconfig:
        config = self.config.EDA_config
        create_directories([config.report_path])

        eda_config = EDAconfig(report_path=config.report_path,df_clean_path= config.df_clean_path)

        return eda_config

    def data_transformation_config(self) ->  DataTransform:
        config  = self.config.DataTransform
        param = self.params.DataTransform
        # create_directories([config.transformed_df_path]) 
        create_directories([config.scaler_path])
        # create_directories([config.pca_model_path])

        data_tra_config = DataTransform(df_path = config.df_path,
                                        test_size=param.test_size,random_state=param.random_state,smote_k_neighbours= param.smote_k_neighbours,
                                        n_pca_components=param.n_pca_components,scaler_path= config.scaler_path,
                                       )
                                 
                                        
        return data_tra_config
    def model_building_config(self):
        config = self.config.model_building
        param = self.params.model_building
        
        model_building_configuration = ModelBuilding(cv = param.cv , random_state= param.random_state,n_iter= param.n_iter , n_jobs = param.n_jobs,
                                                     model_save_path= config.model_save_path,report_save_path= config.report_save_path)
        create_directories([config.model_save_path])
        create_directories([config.report_save_path])
        return model_building_configuration
    
    def prediction_config(self):
        config = self.config.prediction

        prediction_config = Prediction(model_path= config.model_path, scaler_path=config.scaler_path)

        return prediction_config