
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('fraud_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)
    
    # Convert input data into a pandas DataFrame
    transaction = pd.DataFrame(data, index=[0])
    
    # --- Preprocessing Steps ---
    transaction['scaled_amount'] = scaler.transform(transaction['Amount'].values.reshape(-1, 1))
    transaction['scaled_time'] = scaler.transform(transaction['Time'].values.reshape(-1, 1))
    transaction.drop(['Time', 'Amount'], axis=1, inplace=True)
    
    # --- Prediction ---
    prediction = model.predict(transaction)
    prediction_proba = model.predict_proba(transaction)

    # --- Create Response ---
    if prediction[0] == 1:
        response = {
            'status': 'alert',
            'message': 'Fraudulent Transaction Detected!',
            'fraud_probability': f"{prediction_proba[0][1]:.2%}"
        }
    else:
        response = {
            'status': 'ok',
            'message': 'Transaction is Normal.',
            'fraud_probability': f"{prediction_proba[0][1]:.2%}"
        }
        
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
