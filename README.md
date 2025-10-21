# Concrete Pro

**Concrete Pro** is a comprehensive web-based toolkit for civil engineers, students, and construction professionals.  
This application bridges the gap between machine learning and traditional civil engineering by providing three powerful, distinct tools for concrete mix design and analysis.


## ✨ Features

This application offers a complete suite of tools, progressing from simple prediction to advanced, rule-based optimization.

### 1. 🤖 Strength Predictor
A classic machine learning implementation. Input the exact quantities of all 8 concrete components (cement, aggregates, water, etc.) and the curing age, and the pre-trained XGBoost model will predict the resulting compressive strength.

### 2. 📋 Mix Recommender
A fast and reliable tool based on established engineering practices. Select a standard concrete grade (e.g., M25, M40) from a dropdown, and the application provides a cost-aware, practical design-mix recommendation based on a pre-defined table of proven mixes.

### 3. 🧠 Hybrid ML Optimizer
The most advanced feature of the suite.  
This tool uses a hybrid approach that combines engineering standards with machine learning:

- **User Input:** Provide target characteristic strength (e.g., 32.5 MPa) and optional additives.  
- **Baseline Generation:** Finds the closest standard mix as a starting point.  
- **ML Fine-Tuning:** Uses XGBoost and `scipy.optimize` to fine-tune for cost and performance.  
- **Guaranteed Result:** Falls back to baseline mix if optimization fails.


## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Machine Learning:** Scikit-learn, XGBoost, NumPy, Pandas  
- **Optimization:** SciPy  
- **Frontend:** HTML, Bootstrap 5, Jinja2, JavaScript  
- **Deployment:** Gunicorn, Render

---

## 📂 Project Structure

```
concrete-optimizer/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   ├── templates/
│   ├── static/
│
├── ml_model/
│   ├── config.py
│   ├── feature_engineering.py
│   ├── predict.py
│   ├── recommender.py
│   ├── optimize.py
│   └── saved_model/
│
├── .gitignore
├── config.py
├── requirements.txt
└── run.py
```

---

## 🧠 Machine Learning Model

- **Dataset:** UCI Concrete Compressive Strength Data Set (1030 samples)  
- **Engineered Features:**  
  - `binder = Cement + Blast Furnace Slag + Fly Ash`  
  - `aggregate = Coarse Aggregate + Fine Aggregate`  
- **Trained On:** binder, aggregate, water, superplasticizer, and age  
- **Model:** Pre-trained XGBoost Regressor  
- **Author:** Trained and tuned by me
  👉 [GitHub Repository](https://github.com/azhKING69/Opti-Mix)





## 📖 How to Use

- **Homepage:** Overview of all tools  
- **Strength Predictor:** Predict 28-day strength using exact mix proportions  
- **Mix Recommender:** Get standard grade-based design mix instantly  
- **ML Optimizer:** Find optimized cost-effective mix for target strength  

---

## ☁️ Deployment

This app is deployed on **Render**
