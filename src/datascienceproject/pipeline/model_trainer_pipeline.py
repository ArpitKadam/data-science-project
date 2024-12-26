from src.datascienceproject.config.configuration import (ConfigurationManager)
from src.datascienceproject.components.model_trainer import (ModelTrainer)
from src.datascienceproject import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config= model_trainer_config)
        model_trainer.train()

    def __main__():
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = ModelTrainerTrainingPipeline()
            obj.initiate_model_training()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.error(f"Error in {STAGE_NAME} stage: {str(e)}")
            logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<<\n\nx==========x")
            raise e