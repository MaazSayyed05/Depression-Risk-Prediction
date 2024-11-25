from dp_risk_pred.constants import CONFIG_FILE_PATH
from dp_risk_pred.utils.common import read_yaml, create_directories
from dp_risk_pred.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):

        self.config = read_yaml(config_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            zip_path=config.zip_path,
            unzip_path=config.unzip_path,
            raw_data=config.raw_data,
        )

        return data_ingestion_config
