from textSummarizer.pipeline.data_ingestion_1 import DataIngestionPipeline
from textSummarizer.pipeline.data_validation_2 import DataValidationPipeline
from textSummarizer.pipeline.data_transformation_3 import DataTransformationPipeline
from textSummarizer.pipeline.model_trainer_4 import ModelTrainerPipeline
from textSummarizer.pipeline.model_evalution_5 import ModelEvaluationPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> {STAGE_NAME} started  <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>> {STAGE_NAME} completed  <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>> {STAGE_NAME} started  <<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>> {STAGE_NAME} completed  <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>> {STAGE_NAME} started  <<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>> {STAGE_NAME} completed  <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>> {STAGE_NAME} started  <<<<<")
    model_training = ModelTrainerPipeline()
    model_training.main()
    logger.info(f">>>> {STAGE_NAME} completed  <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>> {STAGE_NAME} started  <<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>> {STAGE_NAME} completed  <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e