from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('models/traffic_congestion_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Define congestion level mapping
congestion_map = {'low': 0, 'medium': 1, 'high': 2}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    vehicle_count = data['vehicle_count']
    weather = data['weather']
    road_conditions = data['road_conditions']

    # Preprocess and scale the input
    input_data = scaler.transform([[vehicle_count, weather, road_conditions]])
    prediction = model.predict(input_data)
    
    # Map prediction to numeric level
    congestion_level_numeric = congestion_map[prediction[0]]
    
    return jsonify({'congestion_level': congestion_level_numeric})

if __name__ == '__main__':
    app.run(debug=True)

