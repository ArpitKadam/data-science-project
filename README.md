# 🍷 **Wine Quality Prediction Project** 🍷

[![GitHub](https://img.shields.io/github/stars/ArpitKadam/data-science-project-on-Wine-Quality?style=social)](https://github.com/ArpitKadam/data-science-project-on-Wine-Quality)
[![GitHub issues](https://img.shields.io/github/issues/ArpitKadam/data-science-project-on-Wine-Quality)](https://github.com/ArpitKadam/data-science-project-on-Wine-Quality/issues)
[![License](https://img.shields.io/github/license/ArpitKadam/data-science-project-on-Wine-Quality)](https://github.com/ArpitKadam/data-science-project-on-Wine-Quality/blob/main/LICENSE)

This repository contains a data science project focused on **predicting the quality of wine** based on various chemical properties. Using machine learning, we're exploring the relationship between the characteristics of wine and its perceived quality. 🍇🍷

---

## 🎯 **Project Goal**

The primary goal of this project is to **build a predictive model** that can accurately estimate wine quality based on its chemical composition. By analyzing the data, we aim to:

- Understand the factors that influence wine quality.
- Develop robust machine learning models.
- Gain experience with a typical data science workflow.
- Learn more about **MLOps**.

---

## ⚙️ **Technologies Used**

We used a range of tools to make this project successful, including:

- **Python** 🐍 - Core language for analysis and modeling.
- **Pandas** 📊 - Data manipulation.
- **NumPy** 🔢 - Numerical computing.
- **MLflow** 💻 - Experiment tracking & model management.
- **Dagshub** 🌐 - Versioning and collaboration for MLOps.
- **Flask** 🍂 - For building web APIs.

---

## 🗂️ **Data Overview**

The dataset used in this project is the **Wine Quality dataset**. It contains important chemical features such as:

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- pH
- Sulphates
- Alcohol
- **Quality** (target variable)

You can find the dataset [here](https://github.com/krishnaik06/datasets/raw/refs/heads/main/winequality-data.zip).

---

## 📊 **Project Workflow**

This project follows a well-defined workflow for building and deploying the model:

1. **Data Loading and Exploration** 🧐: Load data using Pandas, explore data types, missing values, and summary statistics.
2. **Model Selection & Training** 🤖: Select ML models (Logistic Regression, ElasticNet, etc.) and train using the data.
3. **Model Evaluation** 🏅: Evaluate the models using **MSE**, **RMSE**, and **R² Score** for performance analysis.
4. **MLOps** 🚀: Implement practices such as Experiment Tracking with MLFlow and Version Control with Dagshub.

---

## 🚀 **Getting Started**

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ArpitKadam/data-science-project-on-Wine-Quality.git
    cd data-science-project-on-Wine-Quality
    ```

2. **Create a virtual environment (recommended)** 💻:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies** 📦:

    ```bash
    pip install -r requirements.txt
    ```

4. **Don't forget to update your Dagshub credentials** 🔑:

    Change the credentials in the following file:

    ```
    data-science-project-on-Wine-Quality
    └── src
        └── datascienceproject
            └── components
                └── model_evaluation.py
    ```

    ```python
    os.environ["MLFLOW_TRACKING_URI"] = '[YOUR_MLFLOW_TRACKING_URI]'
    os.environ["MLFLOW_TRACKING_USERNAME"] = '[YOUR_MLFLOW_TRACKING_USERNAME]'
    os.environ["MLFLOW_TRACKING_PASSWORD"] = '[MLFLOW_TRACKING_PASSWORD]'
    ```

5. **Run the scripts**:

    ```bash
    python main.py
    ```

6. **Run the Flask App** 🍂:

    ```bash
    python app.py
    ```

---

## 🎥 **Demo**

Check out the live demo [here](https://data-science-project-7rcg.onrender.com).

---

## 🤝 **Contributions**

Contributions to this project are welcome! If you have any ideas for improvements, bug fixes, or new features, please feel free to:

- Fork the repository.
- Create a branch for your changes.
- Submit a pull request.

---

## 📄 **License**

This project is licensed under the [MIT License](https://github.com/ArpitKadam/data-science-project-on-Wine-Quality/blob/main/LICENSE).

---

## 📧 **Contact**

Have questions or feedback? Reach out to me at [arpitkadam922@gmail.com](mailto:arpitkadam922@gmail.com) or visit my [GitHub](https://github.com/ArpitKadam).

