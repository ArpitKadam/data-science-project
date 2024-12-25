import os
import urllib.request as request
import zipfile  
from src.datascienceproject import logger
from src.datascienceproject.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data):
            filename, headers = request.urlretrieve(
                url=self.config.source_url, 
                filename=self.config.local_data
            )
            logger.info(f"{filename} downloaded successfully.\nHeaders: {headers}")
        else:
            logger.info(f"File already exists at {self.config.local_data}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted files to {unzip_path}")