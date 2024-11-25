import os, sys
import zipfile
from dp_risk_pred import logger

from dp_risk_pred.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def extract_zip_file(self):
        """
        zip_file_pah: str
        Extarcts the zip file into the  data directory
        Function return None
        """
        # unzip_path = self.config.root_dir
        os.makedirs(self.config.unzip_path, exist_ok=True)
        # logger.info(f"{self.config.local_data_file}")
        with zipfile.ZipFile(self.config.zip_path, "r") as zip_ref:
            zip_ref.extractall(self.config.unzip_path)

            logger.info(f"{self.config.zip_path} unzipped to {self.config.unzip_path}")
