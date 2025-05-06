from breast_cancer.entity.config_entity import EDAconfig
from breast_cancer.config.configuration import ConfigurationManager
from breast_cancer.components.EDA import EDA
from breast_cancer import logger


STAGE_NAME = "EDA"

class EDAPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        eda_config = config.EDA_configuration()
        eda = EDA(config=eda_config)
        eda.perform_eda()


if __name__ == "__main__":
    try:
        logger.info(f">>>>{STAGE_NAME} STARTED<<<<")
        obj = EDAPipeline()
        obj.main()
        logger.info(">>>>{STAGE_NAME} completed<<<<")

    except Exception as e:
        raise e