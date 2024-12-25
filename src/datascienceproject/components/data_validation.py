import os 
from src.datascienceproject import logger
from src.datascienceproject.entity.config_entity import (DataValidationConfig)
import pandas as pd
import numpy as np

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_cols_except_target = list(data.columns)[:-1]

            if all(data[col].dtype == np.float64 for col in all_cols_except_target):
                validation_status = True
                with open(self.config.STATUS_FILE, "w") as file:
                    file.write("All columns are valid")
                logger.info("All columns are valid")
            else:
                validation_status = False
                with open(self.config.STATUS_FILE, "w") as file:
                    file.write("All columns are not valid")
                logger.error("All columns are not valid")
                return validation_status

            if len(all_cols) == 0:
                validation_status = False
                with open(self.config.STATUS_FILE, "w") as file:
                    file.write("No columns in the dataset")
                logger.error("No columns in the dataset")
                return validation_status

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Column {col} not in schema")
                    logger.error(f"Column {col} not in schema") 
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write("All columns are valid")
                    logger.info("All columns are valid")

            return validation_status
        except Exception as e:
            raise e