# 🚗 Car Prediction

## 📌 Summary
This project is a **Machine Learning regression model** that predicts car prices based on various features using advanced algorithms such as XGBoost and CatBoost.  
It demonstrates **data analysis, visualization, ML model training, evaluation, and deployment** techniques.

---

## 📂 Project Structure

```
Car_Prediction/
│── README.md                  # Project documentation
│── car_prediction.ipynb       # Jupyter notebook with code and analysis
│── requirements.txt           # Dependencies
│── car data.csv               # Dataset
│── best_xgb_model.joblib      # Trained XGBoost model
│── catboost_training.json     # CatBoost training metadata
│── model_meta.json            # Model metadata/configuration
│── learn_error.tsv            # CatBoost training error log
│── time_left.tsv              # CatBoost time left info
```

---

## 📊 Dataset
- **Source**: Car price dataset (specify source if known)
- **Size**: Varies (check `car data.csv`)
- **Features**: Various car attributes (e.g., age, mileage, make, model, etc.)
- **Target**: Car price

---

## ⚙️ Technologies Used
- Python 🐍
- Pandas, NumPy (Data Manipulation)
- Matplotlib, Seaborn (Visualization)
- Scikit-learn (Preprocessing & Evaluation)
- XGBoost, CatBoost (Model Training)
- Jupyter Notebook (Analysis & Prototyping)

---

## 🚀 Features

- Data loading, cleaning, and preprocessing
- Exploratory Data Analysis (EDA) and visualization
- Model training using XGBoost and CatBoost
- Model evaluation using RMSE, MAE, and R² Score
- Model persistence for deployment

---

## 🚦 Workflow

1. **Data Preprocessing** → Load and preprocess car dataset  
2. **Exploratory Data Analysis (EDA)** → Visualize feature distributions and relationships  
3. **Model Training** → Train models (XGBoost, CatBoost, etc.)  
4. **Evaluation** → Assess performance using RMSE, MAE, R² Score  
5. **Model Saving** → Export trained models for future use  

---

## ✅ Results

- Achieved high accuracy in predicting car prices.
- XGBoost and CatBoost provided robust performance.
- Model evaluation metrics and error logs are included for transparency.

---

## 💻 How to Run Locally

**Clone this repository:**
```bash
git clone https://github.com/Venkatesh-122/OIBSIP.git
cd Car_Prediction
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Open the Jupyter notebook:**
```bash
jupyter notebook car_prediction.ipynb
```

---

## 📞 Contact

For questions or contributions, open an issue or contact the repository maintainer at **venkateshvenkateah789@gmail.com**.

---

## 📜 License

This project is licensed under the [MIT License](../LICENSE).