# 📧 Spam Detection Project

## 📌 Overview

This project is a Spam Detection System that classifies SMS/email messages as **Spam** or **Ham (Not Spam)**.  
It uses Machine Learning algorithms (**Naive Bayes** & **Logistic Regression**) and compares their performance using confusion matrices and accuracy scores.

The project is implemented in Python, trained using Scikit-learn, and deployed with a simple Streamlit web app for user interaction.

---

## 🚀 Features

- Preprocessing of text messages (cleaning & vectorization)
- Model training with Naive Bayes and Logistic Regression
- Performance evaluation using Confusion Matrix & Accuracy
- Streamlit-based interactive web interface to test custom messages

---

## 🛠️ Tech Stack

- **Python:** NumPy, Pandas, Scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Streamlit
- **Environment:** Google Colab

---

## 📂 Project Structure

```
Spam_Detection/
│── README.md               # Project documentation
│── Spam_prediction.ipynb   # ✅ Training notebook
│── app.py                  # ✅ Streamlit app
│── requirements.txt        # ✅ Dependencies
│── spam.csv                # ✅ Dataset
│── spam_classifier_nb.pkl  # ✅ Saved model (Naive Bayes)
│── vectorizer.pkl          # ✅ Saved vectorizer
```

---

## ⚡ How to Run

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

## 📊 Results

- **Naive Bayes Accuracy:**  
- **Logistic Regression Accuracy:**  

Confusion matrices and accuracy comparison bar charts are included in the notebook.

---

## 📞 Contact

For any questions or contributions, please open an issue or contact the repository maintainer at **venkateshvenkateah789@gmail.com**.

---

## 📜 License

This project is licensed under the [MIT License](../LICENSE).