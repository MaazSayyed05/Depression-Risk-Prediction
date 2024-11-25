
import os,sys
from pathlib import Path
from dp_risk_pred import logger
from dp_risk_pred.config.configuration import ConfigurationManager
from dp_risk_pred.components.data_ingestion import DataIngestion

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.extract_zip_file()
            # logger.info(f'{STAGE_NAME} executed successfully')
        except Exception as e:
            logger.error(f'Error in {STAGE_NAME}: {str(e)}')
            # sys.exit(1)



if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<')
        onj = DataIngestionPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<<<<')

    except Exception as e:
        logger.error(f'Error occurred during {STAGE_NAME}')
        # sys.exit(1)
        logger.exception(e)
        raise e
        