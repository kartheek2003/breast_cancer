from breast_cancer.entity.config_entity import DataTransform
from breast_cancer.config.configuration import ConfigurationManager
from breast_cancer.components.data_transformation import DataTransformation
from breast_cancer import logger

class data_transformation_pipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_tra_config = config.data_transformation_config()
        data_transformation = DataTransformation(config=data_tra_config)
        x_train, x_test, y_train, y_test = data_transformation.get_data_transformation()
        return x_train, x_test, y_train, y_test
        

STAGE_NAME = "data transformation"
if __name__ == "__main__":
    try :
        logger.info(f">>>>{STAGE_NAME} STARTED<<<<")
        obj = data_transformation_pipeline()
        obj.main()
        logger.info(f">>>>{STAGE_NAME} COMPLETED<<<<")

    except Exception as e:
        raise e
       