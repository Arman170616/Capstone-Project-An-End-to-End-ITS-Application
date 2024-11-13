# Traffic Congestion Prediction API

This project is an end-to-end Intelligent Transportation System (ITS) application that predicts traffic congestion levels based on vehicle count, weather, and road conditions. The API is built with Flask, and the model uses scikit-learn's Random Forest Classifier for predictions.

## Features

- **Traffic Congestion Prediction**: Predicts congestion levels as low, medium, or high.
- **REST API Endpoint**: Accepts JSON data and returns predicted congestion level as a numeric value.

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   # Replace 'your-username' with your GitHub username or your repo URL
   git clone https://github.com/your-username/traffic-congestion-predictor.git
   cd traffic-congestion-predictor
Set Up a Virtual Environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Required Packages:

bash
Copy code
pip install -r requirements.txt
Project Structure: Ensure your project has the following structure:

bash
Copy code
├── app.py                  # Flask application for API
├── train_model.py          # Model training script
├── traffic_data.csv        # Dataset for training (sample traffic data)
├── models/
│   ├── traffic_congestion_model.pkl  # Trained model
│   └── scaler.pkl                    # Scaler for data preprocessing
├── requirements.txt       # List of required Python packages
└── README.md              # Project documentation
Model Training
To train the model, ensure your dataset traffic_data.csv includes the necessary fields. Run train_model.py to train and save the model:

Dataset Format: traffic_data.csv should contain the following columns:

vehicle_count
weather (0 for sunny, 1 for rainy, 2 for foggy)
road_conditions (0 for clear, 1 for wet)
congestion_level (target variable: low, medium, or high)
Run the Training Script:

bash
Copy code
python train_model.py
This will generate traffic_congestion_model.pkl and scaler.pkl in the models/ directory.

Running the API
To start the Flask API server:

bash
Copy code
python app.py
The API will be accessible at http://127.0.0.1:5000/.

API Usage
Endpoint
POST /predict

Request Format
Send a JSON payload with the following keys:

vehicle_count (integer): Number of vehicles.
weather (integer): 0 for sunny, 1 for rainy, 2 for foggy.
road_conditions (integer): 0 for clear, 1 for wet.
Example request:

json
Copy code
{
    "vehicle_count": 50,
    "weather": 1,
    "road_conditions": 0
}
Response Format
The API responds with JSON containing the congestion level:

0 for low congestion
1 for medium congestion
2 for high congestion
Example response:

json
Copy code
{
    "congestion_level": 1
}
Dependencies
Install dependencies listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
License
This project is licensed under the MIT License.

Contact
For any questions or issues, please contact:

M M Arman Hossain
Email: armanicepust9@gmail.com
