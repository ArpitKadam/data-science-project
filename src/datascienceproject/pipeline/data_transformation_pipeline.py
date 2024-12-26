from src.datascienceproject.config.configuration import (ConfigurationManager)
from src.datascienceproject.components.data_transformation import (DataTransformation)
from src.datascienceproject import logger
from pathlib import Path


STAGE_NAME = "Data Transformation Stage" 

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f: 
                status = f.read()
            if status == "All columns are valid":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()
            else:
                raise Exception("All columns are not valid")
        except Exception as e:
            logger.error(f"Error in {STAGE_NAME} stage: {str(e)} ")
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} has been started <<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>>>> Stage {STAGE_NAME} has been completed <<<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME} stage: {str(e)} ")
        logger.error(f">>>>>>>> Stage {STAGE_NAME} has been failed <<<<<<<<<\n\nx==========x")
        raise e

