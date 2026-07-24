# House Value Prediction 🏡

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-green)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A machine learning-powered web application that estimates real estate prices based on various house features. Built with **Flask** and **scikit-learn**.

---

## 🚀 Features

* **Accurate Predictions:** Uses a trained regression model to estimate house prices in Lakhs.
* **Dynamic Model Selection:** Training pipeline automatically selects the best-performing model (Linear Regression or Random Forest).
* **Modern UI:** Clean and responsive interface built with Bootstrap 5.
* **Robust Preprocessing:** Handles outliers and categorical encoding automatically.
* **Easy Deployment:** Lightweight Flask application that can be deployed locally or on cloud platforms.

---

## 🛠️ Tech Stack

### Backend

* Flask (Python)

### Machine Learning

* scikit-learn
* Pandas
* NumPy
* joblib

### Frontend

* HTML5
* CSS3
* Bootstrap 5

---

## 🔄 Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Best Model Selection
8. Deployment using Flask

---

## 📋 Prerequisites

* Python 3.10+
* pip (Python Package Manager)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Safin-Bagwan/House-Value-Prediction.git
cd House-Value-Prediction
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Application

### Train the Model (Optional)

If you want to retrain the model using the latest dataset:

```bash
python model_build.py
```

### Start the Flask Server

```bash
python app.py
```

### Access the Web Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📊 Dataset Information

The model is trained on a housing dataset containing the following features:

| Feature           | Description                               |
| ----------------- | ----------------------------------------- |
| Area              | House area in square feet                 |
| Bedrooms          | Number of bedrooms                        |
| Bathrooms         | Number of bathrooms                       |
| Stories           | Number of floors                          |
| Main Road         | Accessibility to main road                |
| Guest Room        | Availability of guest room                |
| Basement          | Presence of basement                      |
| Hot Water Heating | Hot water system availability             |
| Air Conditioning  | AC availability                           |
| Parking           | Number of parking spaces                  |
| Furnishing Status | Furnished, Semi-Furnished, or Unfurnished |

---

## 📈 Model Performance

The application evaluates multiple machine learning algorithms and automatically selects the best-performing model based on evaluation metrics.

Models compared:

* Linear Regression
* Random Forest Regressor

> The best-performing model is saved and used for real-time predictions in the web application.

*You can update this section with your actual R² Score and MAE values after training.*

---

## 📸 Screenshots

### Home Page

```text
Add screenshot here:
screenshots/homepage.png
```

### Prediction Result

```text
Add screenshot here:
screenshots/result.png
```

---

## 📁 Project Structure

```text
House-Value-Prediction/
│
├── app.py
├── model_build.py
├── requirements.txt
│
├── Dataset/
│   └── housing.csv
│
├── ML_Models/
│   ├── model.joblib
│   └── scaler.joblib
│
├── static/
│   ├── style.css
│   └── favicon.ico
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── Notebook/
    └── House_Price_Prediction.ipynb
```

---

## 🚀 Future Improvements

* Deploy the application on Render or AWS.
* Add support for location-based predictions.
* Integrate interactive visualizations and analytics.
* Include advanced ensemble models.
* Build a REST API for external integration.

---

## 👨‍💻 Author

### Safin Bagwan

B.Tech in Computer Science Engineering (AI & Data Science)

GitHub: https://github.com/Safin-Bagwan

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
