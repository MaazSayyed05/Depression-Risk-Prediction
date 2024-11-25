
import os,sys
from pathlib import Path
from dp_risk_pred import logger
from dp_risk_pred.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<')
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f'>>>>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<<<<')

except Exception as e:
    logger.error(f'Error occurred during {STAGE_NAME}')
        # sys.exit(1)
    logger.exception(e)
    raise e

