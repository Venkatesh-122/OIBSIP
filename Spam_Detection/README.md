# 📧 Spam Detection

## 📌 Summary

This project is a **Machine Learning classification model** that detects whether a given SMS/email message is **Spam** or **Ham (Not Spam)**.
It demonstrates **data preprocessing, model training, evaluation, visualization, and deployment** using Streamlit.

---

## 📂 Project Structure

```
Spam_Detection/
│── README.md               # Project documentation
│── Spam_prediction.ipynb   # Jupyter notebook with code and analysis
│── app.py                  # Streamlit web app
│── requirements.txt        # Dependencies
│── spam.csv                # Dataset
│── spam_classifier_nb.pkl  # Trained Naive Bayes model
│── vectorizer.pkl          # TF-IDF vectorizer
```

---

## 📊 Dataset

* **Source**: SMS Spam Collection Dataset
* **Size**: \~5,500 labeled messages
* **Features**: Text message content
* **Target**: Spam (1) / Ham (0)

---

## ⚙️ Technologies Used

* **Python 🐍**
* Pandas, NumPy (Data Handling)
* Scikit-learn (Preprocessing & Model Training)
* Matplotlib, Seaborn (Visualization)
* Streamlit (Deployment & UI)
* Google Colab (Training Environment)

---

## 🚀 Features

* Data cleaning & preprocessing of raw text
* TF-IDF vectorization of messages
* Model training using **Naive Bayes** & **Logistic Regression**
* Evaluation with **Confusion Matrix** & **Accuracy Comparison**
* Streamlit-based interactive app for real-time spam detection

---

## 🚦 Workflow

1. **Data Preprocessing** → Load and clean SMS dataset
2. **Vectorization** → Convert text to numerical features using TF-IDF
3. **Model Training** → Train Naive Bayes & Logistic Regression models
4. **Evaluation** → Confusion Matrices & Accuracy Scores
5. **Deployment** → Streamlit app to test custom messages

---

## ✅ Results

* Models were trained and evaluated on test data.
* Accuracy scores:

- **Naive Bayes Accuracy:**
- **Logistic Regression Accuracy:**
  
* Visual comparisons included in notebook.

---

## 💻 How to Run Locally

**Clone the repository:**

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd Spam_Detection
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

For questions or contributions, open an issue or contact the repository maintainer at **[venkateshvenkateah789@gmail.com](mailto:venkateshvenkateah789@gmail.com)**.

---

## 📜 License

This project is licensed under the [MIT License](../LICENSE).
