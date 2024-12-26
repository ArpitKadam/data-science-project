# 🍷 Wine Quality Prediction Project 🍷

[![GitHub](https://img.shields.io/github/stars/ArpitKadam/data-science-project-on-Wine-Quality?style=social)](https://github.com/ArpitKadam/data-science-project-on-Wine-Quality)
[![GitHub issues](https://img.shields.io/github/issues/ArpitKadam/data-science-project-on-Wine-Quality)](https://github.com/ArpitKadam/data-science-project-on-Wine-Quality/issues)
[![License](https://img.shields.io/github/license/ArpitKadam/data-science-project-on-Wine-Quality)](https://github.com/ArpitKadam/data-science-project-on-Wine-Quality/blob/main/LICENSE)

This repository contains a data science project focused on predicting the quality of wine based on various chemical properties. Using machine learning, we're exploring the relationship between the characteristics of wine and its perceived quality.  Pour yourself a glass and join us on this data-driven journey!

## 🎯 Project Goal

The primary goal of this project is to build a predictive model that can accurately estimate wine quality based on its chemical composition. By analyzing the data, we aim to:

*   Understand the factors that influence wine quality.
*   Develop robust machine learning models.
*   Gain experience with a typical data science workflow.
*   Learn more about MLOperations

## ⚙️ Technologies Used

*   **Python:** The primary programming language for data analysis and model building.
*   **Pandas:** For data manipulation and analysis.
*   **NumPy:** For numerical computations.
*   **MLflow:** For experiment tracking and model management.
*   **Dagshub:** For versioning of data and code, and collaborative MLOps.
*   **pyYAML**: For handling YAML configurations.
*   **notebook**: For interactive coding using jupyter notebooks.
*   **python-box**: For working with dictionaries and configurations more easily
*   **ensure**: For type checking
*   **joblib**: For saving machine learning models
*   **Flask**: For building web application APIs
*   **Flask-Cors**: For cross origin request management


## 🗂️ Data

The dataset used in this project is the "Wine Quality" dataset. It contains features such as:

*   Fixed Acidity
*   Volatile Acidity
*   Citric Acid
*   Residual Sugar
*   Chlorides
*   Free Sulfur Dioxide
*   Total Sulfur Dioxide
*   Density
*   pH
*   Sulphates
*   Alcohol
*   Quality (target variable)

The data was likely downloaded from [GitHub Machine Learning Datasets](https://github.com/krishnaik06/datasets/raw/refs/heads/main/winequality-data.zip) .

## 📊 Project Workflow

Here's a high-level overview of the steps taken in this project:

1.  **Data Loading and Exploration:** Loading the data using Pandas and performing initial data exploration, such as identifying data types, checking for missing values, and summary statistics.
2.  **Model Selection and Training:** Choosing appropriate machine learning models (e.g., Logistic Regression, ElasticNet, Decision Trees, etc.) and training them using the prepared dataset.
3.  **Model Evaluation:**  Evaluating model performance using appropriate metrics (e.g.,MSE, RMSE, MAS, R2_SCORE for regression)
4.  **MLOps (Machine Learning Operations):** Implementing MLOps practices to streamline the model lifecycle. This may include:
    *   **Model Packaging:** Saving the trained model for easy deployment (e.g., using `pickle` or `joblib`).
    *   **Experiment Tracking:** Logging model parameters, metrics and artifacts (e.g. Using MLFlow).
    *   **Version Control:** Managing changes to models, code, and datasets using [Dagshub](https://dagshub.com/dashboard).
    *   **Model Deployment:**  Exploring possibilities for deploying the model as an API or service, (I have used Flask and [Render.com](https://render.com/)).


## 🚀 Getting Started

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ArpitKadam/data-science-project-on-Wine-Quality.git
    cd data-science-project-on-Wine-Quality
    ```
2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```
3.  **Install required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
4.  **Remeber to change the Dagshub Credentials in this folder**
   
    ```
    data-science-project-on-Wine-Quality
    |-\src
        |-\datascienceproject
                     |-\components
                            |-model_evaluation.py
    ```
    ```python
    os.environ["MLFLOW_TRACKING_URI"] = '[YOUR_MLFLOW_TRACKING_URI]'
    os.environ["MLFLOW_TRACKING_USERNAME"] = '[YOUR_MLFLOW_TRACKING_USERNAME]'
    os.environ["MLFLOW_TRACKING_PASSWORD"] = '[MLFLOW_TRACKING_PASSWORD]'
    ```   
5.  **Run the scripts:**

    ```bash
    python main.py
    ```
6.  **Run the Flask App**

    ```bash
    python app.py
    ```

##  Demo
https://data-science-project-7rcg.onrender.com

## 🤝 Contributions

Contributions to this project are welcome! If you have any ideas for improvements, bug fixes, or new features, please feel free to:

*   Fork the repository.
*   Create a branch for your changes.
*   Submit a pull request.

## 📄 License

This project is licensed under the [MIT License](https://github.com/ArpitKadam/data-science-project-on-Wine-Quality/blob/main/LICENSE).

## 📧 Contact

If you have any questions or suggestions, feel free to reach out to me: [arpitkadam922@gmail.com / https://github.com/ArpitKadam].
