from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import psycopg2
import json
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load the trained model
model = joblib.load('model.pkl')

# Load the scaler and label encoders used during preprocessing
scaler = joblib.load('scaler.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# PostgreSQL connection parameters
db_params = {
    'dbname': 'credit_scoring',
    'user': 'postgres',  # Replace with your PostgreSQL username
    'password': 'Pandavas@123',  # Replace with your PostgreSQL password
    'host': 'localhost'
}


def save_prediction(features, prediction):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO predictions (features, prediction) VALUES (%s, %s)",
                       (json.dumps(features), prediction))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        logging.error(f"Error saving prediction: {e}")


@app.route('/')
def home():
    return "Credit Scoring Model API"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = pd.DataFrame([data['features']])

        # Preprocess the features the same way as during training
        for column, encoder in label_encoders.items():
            features[column] = encoder.transform(features[column])

        numerical_features = features.select_dtypes(include=['int64', 'float64']).columns
        features[numerical_features] = scaler.transform(features[numerical_features])

        # Make prediction
        prediction = model.predict(features)

        # Save the prediction to the database
        save_prediction(data['features'], int(prediction[0]))

        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        logging.error(f"Error making prediction: {e}")
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
