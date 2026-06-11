# 🚀 Customer Churn Prediction API

A Machine Learning project that predicts whether a customer is likely to **churn (leave the service)** based on customer attributes such as tenure, monthly charges, support calls, contract type, internet service, payment method, and senior citizen status.

The trained model is deployed using **FastAPI** and hosted on **Render**, providing real-time predictions through a REST API.

---

## 📌 Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses. Predicting customers who are likely to leave helps companies take proactive measures to retain them.

This project demonstrates an end-to-end Machine Learning workflow:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Model training and evaluation
* Model explainability using SHAP
* API development with FastAPI
* Cloud deployment on Render

---

## 🎯 Problem Statement

**Target Variable:**

* `Churn`

  * `1` → Customer will churn
  * `0` → Customer will stay

The objective is to accurately predict customer churn so businesses can improve retention strategies.

---

## 📊 Exploratory Data Analysis (EDA)

The dataset was analyzed for:

* Missing values
* Feature distributions
* Class balance
* Numerical and categorical variables
* Data quality issues

Visualizations and summaries were used to understand customer behavior before model training.

---

## ⚙️ Data Preprocessing

The preprocessing pipeline includes:

* Handling missing values using imputers
* Encoding categorical variables
* Preparing numerical features
* Combining preprocessing and model into a Scikit-learn Pipeline

This ensures consistent preprocessing during both training and prediction.

---

## 🤖 Models Trained

Three classification models were evaluated:

1. Logistic Regression
2. Random Forest Classifier
3. Gradient Boosting Classifier

Performance was compared using multiple evaluation metrics instead of relying only on accuracy.

---

## 📈 Model Evaluation

Metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

ROC-AUC was considered an important metric because churn datasets may have class imbalance, making accuracy alone insufficient.

---

## 🔍 Model Explainability (SHAP)

SHAP (SHapley Additive exPlanations) was used to understand feature importance.

The SHAP summary plot highlights how different features contribute to predicting customer churn.

Key influential features include:

* Tenure
* Monthly Charges
* Support Calls
* Contract Type
* Internet Service

This improves transparency and interpretability of the model.

---

## 🌐 FastAPI Deployment

The trained model is saved using **Joblib** and loaded **once at application startup**.

Features:

* POST `/predict` endpoint
* Pydantic input validation
* Automatic Swagger documentation
* JSON request/response format
* Clean validation errors for invalid input

---

## 🚀 Live API

Base URL:

```
https://customer-churn-prediction-1-xrgd.onrender.com
```

Swagger Documentation:

```
https://customer-churn-prediction-1-xrgd.onrender.com/docs
```

---

## 📥 Sample Request

```json
{
  "tenure_months": 12,
  "monthly_charges": 1200,
  "support_calls": 2,
  "contract": "Month-to-month",
  "internet_service": "Fiber",
  "payment_method": "Electronic check",
  "senior_citizen": 0
}
```

---

## 📤 Sample Response

```json
{
  "prediction": 1,
  "churn_probability": 0.9998
}
```

Where:

* `prediction = 1` → Customer is likely to churn
* `prediction = 0` → Customer is likely to stay

---

## 📂 Project Structure

```
customer-churn-prediction/
│
├── app.py
├── customer_churn_model.joblib
├── requirements.txt
├── Dockerfile
├── .python-version
├── README.md
├── customer_churn.csv
├── training_notebook.ipynb
└── screenshots/
```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
cd customer-churn-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API locally:

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t customer-churn-api .
```

Run the container:

```bash
docker run -p 8000:8000 customer-churn-api
```

---

## 📦 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* SHAP
* Joblib
* FastAPI
* Pydantic
* Uvicorn
* Render

---

## 📸 Screenshots to Include

* Project Structure
* Model Evaluation Results
* SHAP Summary Plot
* Swagger Documentation
* API Request
* API Response
* Render Deployment Status

---

## 📚 Key Learnings

* Data preprocessing using pipelines
* Classification model comparison
* Model evaluation with multiple metrics
* Explainable AI using SHAP
* Building REST APIs with FastAPI
* Deploying Machine Learning models to the cloud
* Serving predictions in real time

---

## 👨‍💻 Author

**Aakkash D M**

Machine Learning • Data Science • Artificial Intelligence • FastAPI

---

## ⭐ Future Improvements

* Authentication for API endpoints
* Batch prediction support
* Database integration
* Monitoring and logging
* CI/CD pipeline
* Frontend dashboard for predictions
