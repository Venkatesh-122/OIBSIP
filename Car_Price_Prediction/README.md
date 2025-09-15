```markdown
# 🚗 Car Price Prediction

## 📌 Summary

This project is a **Machine Learning regression model** that predicts car prices based on multiple features using advanced algorithms such as **XGBoost** and **CatBoost**.  
It demonstrates **data preprocessing, feature engineering, visualization, model training, evaluation, and explainability** using SHAP.

---

## 📂 Project Structure

```

Car\_Prediction/
│── README.md                  # Project documentation
│── app.py                     # Streamlit app for car price prediction
│── car\_prediction.ipynb       # Jupyter notebook with code and analysis
│── requirements.txt           # Dependencies
│── car data.csv               # Dataset
│── best\_xgb\_model.joblib      # Trained XGBoost model

````

---

## 📊 Dataset

* **Source**: Car price dataset (`car data.csv`)  
* **Size**: Few thousand rows (tabular data)  
* **Features**:  
  - Car Age  
  - Present Price  
  - Driven Kilometers  
  - Fuel Type  
  - Transmission  
  - Owner history  
* **Target**: `Selling_Price` (car price)

---

## ⚙️ Technologies Used

* **Python 🐍**  
* Pandas, NumPy (Data Handling)  
* Matplotlib, Seaborn (Visualization)  
* Scikit-learn (Preprocessing & Evaluation)  
* XGBoost, CatBoost (Model Training)  
* SHAP (Model Explainability)  
* Jupyter Notebook (Development & Analysis)  
* Streamlit (Deployment & UI)  

---

## 🚀 Features

* Data loading, cleaning, and preprocessing  
* Outlier detection and handling  
* Exploratory Data Analysis (EDA)  
* Feature engineering (Car Age, Brand extraction, log transforms)  
* Model training with **XGBoost** and **CatBoost**  
* Evaluation using **RMSE, MAE, R² Score**  
* Model persistence (`joblib` export) for deployment  
* Explainable AI with **SHAP values**  

---

## 🚦 Workflow

1. **Data Preprocessing** → Load, clean, and prepare the dataset  
2. **Exploratory Data Analysis (EDA)** → Visualize distributions and correlations  
3. **Feature Engineering** → Derive features like car age and brand  
4. **Model Training** → Train regression models (XGBoost, CatBoost, etc.)  
5. **Evaluation** → Assess models with RMSE, MAE, R² Score  
6. **Explainability** → Use SHAP to understand feature impact  
7. **Deployment** → Save and use models in a Streamlit app  

---

## ✅ Results

* Achieved **high accuracy** in predicting car prices  
* **XGBoost and CatBoost** performed best  
* SHAP analysis showed:  
  - **Present Price** and **Car Age** are the most influential features  
* Metrics and plots available in the notebook  

---

## 💻 How to Run Locally

**Clone the repository:**

```bash
git clone https://github.com/Venkatesh-122/OIBSIP.git
cd Car_Prediction
````

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run the Jupyter Notebook:**

```bash
jupyter notebook car_prediction.ipynb
```

**Run the Streamlit App:**

```bash
streamlit run app.py
```

---

## 📞 Contact

For questions or contributions, open an issue or contact the repository maintainer at **[venkateshvenkateah789@gmail.com](mailto:venkateshvenkateah789@gmail.com)**.

---

## 📜 License

This project is licensed under the [MIT License](../LICENSE).
