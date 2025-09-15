```markdown
# 🚗 Car Price Prediction

## 📌 Summary
This project builds a **Machine Learning regression model** that predicts car prices based on multiple features using advanced algorithms such as **XGBoost** and **CatBoost**.  
It demonstrates **data preprocessing, feature engineering, visualization, model training, evaluation, and explainability** using SHAP.

---

## 📂 Project Structure

Car_Prediction/
│── README.md                  # Project documentation
│── app.py                     # Streamlit app for car price prediction
│── car_prediction.ipynb       # Jupyter notebook with code and analysis
│── requirements.txt           # Dependencies
│── car data.csv               # Dataset
│── best_xgb_model.joblib      # Trained XGBoost model

---

## 📊 Dataset
- **Source**: Car price dataset (`car data.csv`)  
- **Size**: Few thousand rows (tabular data)  
- **Features**: Car attributes such as:
  - Car Age
  - Present Price
  - Driven Kilometers
  - Fuel Type
  - Transmission
  - Owner history  
- **Target**: `Selling_Price` (car price)

---

## ⚙️ Technologies Used
- **Python** 🐍
- **Pandas, NumPy** → Data manipulation  
- **Matplotlib, Seaborn** → Data visualization  
- **Scikit-learn** → Preprocessing & evaluation  
- **XGBoost, CatBoost** → Model training  
- **SHAP** → Model explainability  
- **Jupyter Notebook** → Development & analysis  

---

## 🚀 Features

- Data loading, cleaning, and preprocessing  
- Outlier detection and handling  
- Exploratory Data Analysis (EDA)  
- Feature engineering (e.g., Car Age, Brand extraction, log transforms)  
- Model training with **XGBoost** and **CatBoost**  
- Model evaluation using **RMSE, MAE, R² Score**  
- Model persistence (`joblib` export) for deployment  
- Explainable AI with **SHAP values**  

---

## 🚦 Workflow

1. **Data Preprocessing** → Load, clean, and prepare the dataset  
2. **Exploratory Data Analysis (EDA)** → Visualize distributions and feature correlations  
3. **Feature Engineering** → Derive useful features like car age and brand  
4. **Model Training** → Train regression models (XGBoost, CatBoost, etc.)  
5. **Evaluation** → Assess models with RMSE, MAE, R² Score  
6. **Explainability** → Use SHAP to understand feature impact  
7. **Model Saving** → Save best models for deployment  

---

## ✅ Results

- Achieved **high accuracy** in predicting car prices.  
- **XGBoost and CatBoost** delivered robust performance.  
- SHAP analysis showed:
  - **Present Price** and **Car Age** are the most influential features.  
- Model metrics and error logs are available for transparency.  

---

## 📊 SHAP Explainability

SHAP was used to explain model predictions:  
- **Bar plots** and **beeswarm plots** show feature importance.  
- **Dependence plots** highlight how individual features affect predictions.  
- **Force plots** provide local explanations for single predictions.  

⚠️ **Note on SHAP Visualizations**  
Some SHAP plots (bar, beeswarm, dependence) are fully visible on GitHub.  
However, **force plots require JavaScript**, which GitHub disables for security.  
You may see this warning:

```

Visualization omitted, Javascript library not loaded!

````

👉 This is expected and **not an error in your code**.  
To view interactive force plots, run the notebook locally in **Jupyter Notebook** or **Google Colab**.  

---

## 💻 How to Run Locally

Clone the repository:
```bash
git clone https://github.com/Venkatesh-122/OIBSIP.git
cd Car_Prediction
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Jupyter notebook:

```bash
jupyter notebook car_prediction.ipynb
```

---

## 📞 Contact

For questions, suggestions, or contributions, please open an **issue**
or contact the maintainer: **[venkateshvenkateah789@gmail.com](mailto:venkateshvenkateah789@gmail.com)**

---

## 📜 License

This project is licensed under the [MIT License](../LICENSE).

