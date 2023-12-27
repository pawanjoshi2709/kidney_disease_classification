from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01 import DataIngestionTrainingPipeline

STAGE_NAME = "data ingestion stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<")    
except Exception as e:
    logger.exception(e)
    raise e