from src.datascienceproject.config.configuration import (ConfigurationManager)
from src.datascienceproject.components.model_evaluation import (ModelEvaluation)
from src.datascienceproject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config= model_evaluation_config)
        model_evaluation.log_into_mlflow()

    def __main__():
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = ModelEvaluationTrainingPipeline()
            obj.initiate_model_evaluation()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.error(f"Error in {STAGE_NAME} stage: {str(e)}")
            logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<<\n\nx==========x")
            raise e