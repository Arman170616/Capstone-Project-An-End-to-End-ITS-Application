#!/bin/bash

# Traffic Congestion Prediction API

This project is an end-to-end Intelligent Transportation System (ITS) application that predicts traffic congestion levels based on vehicle count, weather, and road conditions. The API is built with Flask, and the model uses scikit-learn's Random Forest Classifier for predictions.

## Features

- **Traffic Congestion Prediction**: Predicts congestion levels as low, medium, or high.
- **REST API Endpoint**: Accepts JSON data and returns predicted congestion level as a numeric value.

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Setup and Installation

1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/your-username/traffic-congestion-predictor.git
   cd traffic-congestion-predictor
   \`\`\`

2. **Set up a virtual environment**:
   \`\`\`bash
   python -m venv env
   source env/bin/activate  # On Windows use \`env\Scripts\activate\`
   \`\`\`

3. **Install required packages**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Folder Structure**:
   Make sure your project has the following structure:

   \`\`\`
   ├── app.py                  # Flask app
   ├── train_model.py          # Model training script
   ├── traffic_data.csv        # Sample traffic data file for training
   ├── models/
   │   ├── traffic_congestion_model.pkl  # Trained model
   │   └── scaler.pkl                    # Scaler for input data
   ├── requirements.txt       # Required Python packages
   └── README.md              # Project documentation
   \`\`\`

## Model Training

If you need to retrain the model, you can use the \`train_model.py\` script.

1. Ensure you have a CSV file named \`traffic_data.csv\` with the following columns:
   - \`vehicle_count\`
   - \`weather\` (encoded as \`0\` for sunny, \`1\` for rainy, \`2\` for foggy)
   - \`road_conditions\` (encoded as \`0\` for clear, \`1\` for wet)
   - \`congestion_level\` (target variable, categorical: \`low\`, \`medium\`, or \`high\`)

2. Run the training script:
   \`\`\`bash
   python train_model.py
   \`\`\`

   This will save the trained model and scaler in the \`models/\` directory.

## Running the API

To start the Flask API, run the following command:

\`\`\`bash
python app.py
\`\`\`

The API will be accessible at \`http://127.0.0.1:5000/\`.

## API Usage

### Endpoint

\`POST /predict\`

### Request Format

Send a JSON payload with the following keys:

- \`vehicle_count\`: (integer) The number of vehicles.
- \`weather\`: (integer) \`0\` for sunny, \`1\` for rainy, \`2\` for foggy.
- \`road_conditions\`: (integer) \`0\` for clear, \`1\` for wet.

Example request:

\`\`\`json
{
    "vehicle_count": 50,
    "weather": 1,
    "road_conditions": 0
}
\`\`\`

### Response Format

The API will respond with a JSON object containing the predicted congestion level as a numeric value:

- \`0\` for low congestion
- \`1\` for medium congestion
- \`2\` for high congestion

Example response:

\`\`\`json
{
    "congestion_level": 1
}
\`\`\`

## Dependencies

All dependencies are listed in \`requirements.txt\`. You can install them with:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, please contact:

**M M Arman Hossain**  
Email: [armanicepust9@gmail.com](mailto:armanicepust9@gmail.com)

EOL

# Notify user of successful README creation
echo "README.md has been successfully created!"