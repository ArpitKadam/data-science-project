from src.datascienceproject.constants import *
from src.datascienceproject.utils.common import read_yaml, create_directories
from src.datascienceproject.entity.config_entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(self, 
                 config_filepath=CONFIG_FILE_PATH, 
                 params_filepath=PARAMS_FILE_PATH, 
                 schema_filepath=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        ##print("Debug Config:", self.config)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        # Validate configuration structure
        if "artifacts" not in self.config or "artifacts_root" not in self.config["artifacts"]:
            raise KeyError("'artifacts_root' is missing in the configuration.")

        # Create root directory
        create_directories([self.config["artifacts"]["artifacts_root"]])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]  # Corrected access
        create_directories([config["root_dir"]])

        # Create DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            source_URL=config["source_url"],
            local_data_file=Path(config["local_data"]),
            unzip_dir=Path(config["unzip_dir"])
        )
        return data_ingestion_config