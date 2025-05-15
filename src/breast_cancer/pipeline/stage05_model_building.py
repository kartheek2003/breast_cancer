from breast_cancer.config.configuration import ConfigurationManager
from breast_cancer.components.model_building import ModelBuildingComponent
from breast_cancer import logger

class ModelBuildingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_building = config.model_building_config()
        model_building_comp = ModelBuildingComponent(config=model_building)
        model_building_comp.model()



STAGE_NAME = "MODEL BUILDING"

if __name__ == "__main__":
    try :
        logger.info(f">>>>{STAGE_NAME} STARTED<<<<")
        obj = ModelBuildingPipeline()
        obj.main()
        logger.info(f">>>>{STAGE_NAME} COMPLETED<<<<")

    except Exception as e:
        raise e

    