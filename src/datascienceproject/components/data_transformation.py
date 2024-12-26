import os
from src.datascienceproject import logger
from sklearn.model_selection import train_test_split
from src.datascienceproject.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Data split completed.")
        logger.info(f"Train shape: {train.shape},\n Test shape: {test.shape}")

        print(f"Train shape: {train.shape},\n Test shape: {test.shape}")