# 🌸 Iris Flower Prediction

## 📌 Summary
This project is a **Machine Learning classification model** that predicts the species of Iris flowers (*Setosa, Versicolor, Virginica*) with ~97% accuracy using **Scikit-learn**.  
It demonstrates **data analysis, visualization, ML model training, evaluation, and deployment** using **Streamlit + ngrok**.

---

## 📂 Project Structure

```
Iris_Flower_Prediction/
│── README.md                 # Project documentation
│── iris_flower_prediction.ipynb  # Jupyter notebook with code and analysis
│── app.py                    # Streamlit web application
│── requirements.txt          # Dependencies
│── iris.csv                  # Dataset

```

---

## 📊 Dataset
- **Source**: Iris dataset (UCI ML Repository / scikit-learn)
- **Size**: 150 rows, 4 features, 1 target column
- **Features**: Sepal Length, Sepal Width, Petal Length, Petal Width
- **Target**: Species (*Setosa, Versicolor, Virginica*)

---

## ⚙️ Technologies Used
- Python 🐍
- Pandas, NumPy
- Matplotlib, Seaborn (Visualization)
- Scikit-learn (ML Models & Evaluation)
- Streamlit (Web UI)
- ngrok (Deployment & Sharing)

---

## 🚀 Features

- Data loading, preprocessing, and EDA (Exploratory Data Analysis)
- Visualizations: Pairplots, heatmaps, feature distributions
- Model training with Logistic Regression, Random Forest, SVM, etc.
- Evaluation: Accuracy score, confusion matrix
- User-friendly Streamlit web interface for predictions
- Public app sharing with ngrok

---

## 🚦 Workflow

1. **Data Exploration** → Load and analyze Iris dataset  
2. **Visualization** → Pairplots, heatmaps, distributions  
3. **Model Training** → Logistic Regression, Random Forest, SVM, etc.  
4. **Evaluation** → Accuracy score, confusion matrix  
5. **Deployment** → Streamlit app with public link via ngrok  

---

## ✅ Results

- Achieved **97–100% accuracy** on test data.
- **Random Forest & SVM** gave the best performance.
- Model performance visualized via confusion matrix and bar charts.

---

## 💻 How to Run Locally

**Clone this repository:**
```bash
git clone https://github.com/Venkatesh-122/OIBSIP.git
cd Iris_Flower_Prediction
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the Streamlit app:**
```bash
streamlit run app.py
```

---

## 📞 Contact

For questions or contributions, open an issue or contact the repository maintainer at **venkateshvenkateah789@gmail.com**.

---

## 📜 License

This project is licensed under the [MIT License](../LICENSE).