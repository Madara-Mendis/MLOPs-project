from MLOpsProject import logger
from MLOpsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLOpsProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MLOpsProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from MLOpsProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from MLOpsProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_validation_pipeline = DataValidationTrainingPipeline()
        data_validation_pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

 
STAGE_NAME = "Data Transformation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_transformation_pipeline = DataTransformationTrainingPipeline()
        data_transformation_pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

 
STAGE_NAME = "Model Trainer Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_trainer_pipieline = ModelTrainerTrainingPipeline()
        model_trainer_pipieline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Evaluation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_trainer_pipieline = ModelEvaluationTrainingPipeline()
        model_trainer_pipieline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
          
    