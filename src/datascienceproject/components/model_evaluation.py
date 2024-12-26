import os
import mlflow
import pandas as pd
import mlflow.sklearn
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, root_mean_squared_error
from urllib.parse import urlparse
import joblib 
from mlflow.models import infer_signature
from src.datascienceproject.entity.config_entity import ModelEvaluationConfig 
from src.datascienceproject.constants import *
from src.datascienceproject.utils.common import read_yaml, create_directories, save_json

os.environ["MLFLOW_TRACKING_URI"] = 'https://dagshub.com/ArpitKadam/data-science-project.mlflow'
os.environ["MLFLOW_TRACKING_USERNAME"] = 'ArpitKadam'
os.environ["MLFLOW_TRACKING_PASSWORD"] = '5989d6b56c4eec6ea090d927851d1fb5297a42a8'

class ModelEvaluation: 
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        mse = mean_squared_error(actual, pred)
        rmse = root_mean_squared_error(actual, pred)
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return mse, rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        x_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_registry_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(x_test)

            (mse, rmse, mae, r2) = self.eval_metrics(y_test, predicted_qualities)

            scores = {"mse": mse, "rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metrics({"mse": mse, "rmse": rmse, "mae": mae, "r2": r2})

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel_2.0")
            else:
                mlflow.sklearn.log_model(model, "model")

            mlflow.end_run()