from src.datascienceproject.config.configuration import (ConfigurationManager)
from src.datascienceproject.components.data_validation import (DataValidation)
from src.datascienceproject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

    def __main__():
        try:
            logger.info(f">>>>>>>> Stage {STAGE_NAME} has been started <<<<<<<<<")
            obj = DataValidationTrainingPipeline()
            obj.initiate_data_validation()
            logger.info(f">>>>>>>> Stage {STAGE_NAME} has been completed <<<<<<<<<\n\nx==========x")
        except Exception as e:
            logger.error(f"Error in {STAGE_NAME} stage: {str(e)} ")
            logger.error(f">>>>>>>> Stage {STAGE_NAME} has been failed <<<<<<<<<\n\nx==========x")
            raise e 
