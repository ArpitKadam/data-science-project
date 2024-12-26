from src.datascienceproject import logger
from src.datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascienceproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascienceproject.pipeline.data_transformation_pipeline import  DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx==========x")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME} stage: {str(e)}")
    logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<< \n\nx==========x")
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx==========x")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME} stage: {str(e)}")
    logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<< \n\nx==========x")
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>>> Stage {STAGE_NAME} has been started <<<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} has been completed <<<<<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME} stage: {str(e)} ")
    logger.error(f">>>>>>>> Stage {STAGE_NAME} has been failed <<<<<<<<<\n\nx==========x")
    raise e