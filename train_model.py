import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# Load traffic data (make sure the CSV file is present in the same folder)
df = pd.read_csv("traffic_data.csv")

# Feature engineering: Convert categorical data to numerical data
df['weather'] = df['weather'].map({'sunny': 0, 'rainy': 1, 'foggy': 2})
df['road_conditions'] = df['road_conditions'].map({'clear': 0, 'wet': 1})

# Select features and target
features = ['vehicle_count', 'weather', 'road_conditions']
target = 'congestion_level'

X = df[features]
y = df[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save the model and the scaler
joblib.dump(model, 'models/traffic_congestion_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')

print("Model and scaler saved successfully.")
