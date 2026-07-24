from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model and scaler
model_lr = joblib.load('ML_Models/model.joblib')
scaler = joblib.load('ML_Models/scaler.joblib')

# Prediction function
def predict_price(input_data):
    # Convert to DataFrame
    data = pd.DataFrame(input_data, index=[0])

    # Binary mapping
    yes_no_attributes = [
        'mainroad', 'guestroom', 'basement',
        'hotwaterheating', 'airconditioning',
        'prefarea', 'furnishingstatus_semi-furnished',
        'furnishingstatus_unfurnished'
    ]
    mapping = {'yes': 1, 'no': 0}
    for col in yes_no_attributes:
        data[col] = data[col].map(mapping)

    # Scale numeric columns
    non_bin_vars = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
    data[non_bin_vars] = scaler.transform(data[non_bin_vars])

    # Prediction
    return model_lr.predict(data)[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get raw inputs
    furnishing_status = request.form['furnishing_status']
    area = int(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    stories = int(request.form['stories'])
    parking = int(request.form['parking'])

    # Validate non-negative numeric inputs
    if area <= 0 or bedrooms < 0 or bathrooms < 0 or stories < 0 or parking < 0:
        error = "Error: Values must be positive numbers!"
        return render_template('index.html', error=error)

    # Map furnishing status
    if furnishing_status == 'furnished':
        semi_furnished = 'no'
        unfurnished = 'no'
    elif furnishing_status == 'semi-furnished':
        semi_furnished = 'yes'
        unfurnished = 'no'
    else:
        semi_furnished = 'no'
        unfurnished = 'yes'

    # Gather all inputs
    input_data = {
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'stories': stories,
        'mainroad': request.form['mainroad'],
        'guestroom': request.form['guestroom'],
        'basement': request.form['basement'],
        'hotwaterheating': request.form['hotwaterheating'],
        'airconditioning': request.form['airconditioning'],
        'parking': parking,
        'prefarea': request.form['prefarea'],
        'furnishingstatus_semi-furnished': semi_furnished,
        'furnishingstatus_unfurnished': unfurnished
    }

    # Get price
    try:
        price = round(predict_price(input_data), 2)
        return render_template('index.html', prediction=price)
    except Exception as e:
        return render_template('index.html', error=f"Error predicting price: {e}")

if __name__ == '__main__':
    app.run(debug=True)
