from flask import Flask, render_template, request
import os
import numpy as np
import joblib
import pandas as pd
from src.datascienceproject.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/train',methods=['GET'])
def train():
    os.system('python main.py')
    return "Training Completed"

@app.route('/predict',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])
            
            data = [fixed_acidity, volatile_acidity, citric_acid, 
                    residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, 
                    density, pH, sulphates, alcohol]
            
            data = np.array(data).reshape(1,11)

            obj = PredictionPipeline(model_path='./artifacts/model_trainer/model.joblib')
            predict = obj.predict(data)

            return render_template('result.html', prediction = str(predict),
                                    fixed_acidity = str(fixed_acidity), volatile_acidity = str(volatile_acidity),
                                    citric_acid = str(citric_acid), residual_sugar = str(residual_sugar),
                                    chlorides = str(chlorides), free_sulfur_dioxide = str(free_sulfur_dioxide),
                                    total_sulfur_dioxide = str(total_sulfur_dioxide), density = str(density),
                                    pH = str(pH), sulphates = str(sulphates), alcohol = str(alcohol))

        except Exception as e:
            return 'Error: {}'.format(e)
    else:   
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)