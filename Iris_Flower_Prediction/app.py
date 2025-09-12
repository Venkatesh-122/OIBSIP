import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# 1. Load Data
iris = load_iris(as_frame=True)
X = iris.data
y = iris.target
target_names = iris.target_names

st.title("🌸 Iris Flower Classification: Logistic Regression vs SVM")
st.write("This app compares **Logistic Regression** and **SVM** on the Iris dataset using hyperparameter tuning, cross-validation, and visualizations.")

# 2. Hyperparameter Tuning

param_grid_lr = [
    {"penalty": ["l2"], "C": [0.01, 0.1, 1, 10, 100], "solver": ["lbfgs", "saga"]},
    {"penalty": ["l1"], "C": [0.01, 0.1, 1, 10, 100], "solver": ["liblinear", "saga"]},
    {"penalty": ["elasticnet"], "C": [0.01, 0.1, 1, 10, 100], "solver": ["saga"], "l1_ratio": [0.1, 0.5, 0.9]},
]

param_grid_svm = {
    "C": [0.1, 1, 10, 100],
    "kernel": ["linear", "rbf", "poly"],
    "gamma": ["scale", "auto"]
}

grid_lr = GridSearchCV(LogisticRegression(max_iter=5000, random_state=42), param_grid_lr, cv=5, scoring="accuracy", n_jobs=-1)
grid_svm = GridSearchCV(SVC(probability=True, random_state=42), param_grid_svm, cv=5, scoring="accuracy", n_jobs=-1)

grid_lr.fit(X, y)
grid_svm.fit(X, y)

# Best models
best_lr = grid_lr.best_estimator_
best_svm = grid_svm.best_estimator_

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

best_lr.fit(X_train, y_train)
best_svm.fit(X_train, y_train)

# 4. Cross-Validation Scores
lr_cv_scores = cross_val_score(best_lr, X, y, cv=5, scoring="accuracy")
svm_cv_scores = cross_val_score(best_svm, X, y, cv=5, scoring="accuracy")

cv_results = pd.DataFrame({
    "Logistic Regression": lr_cv_scores,
    "SVM": svm_cv_scores
})

# 5. Visualize CV Results
st.subheader("Cross-Validation Comparison")

# Boxplot
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.boxplot(data=cv_results, palette="Set2", ax=ax1)
ax1.set_title("Cross-Validation Accuracy Comparison")
ax1.set_ylabel("Accuracy")
st.pyplot(fig1)
plt.close(fig1)

# Bar chart (mean accuracy)
fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.barplot(
    x=cv_results.mean().index,
    y=cv_results.mean().values,
    hue=cv_results.mean().index,
    dodge=False,
    palette="Set2",
    legend=False,
    ax=ax2
)
ax2.set_title("Mean CV Accuracy")
ax2.set_ylabel("Accuracy")
ax2.set_ylim(0.9, 1.0)
for i, v in enumerate(cv_results.mean().values):
    ax2.text(i, v + 0.002, f"{v:.3f}", ha="center", fontsize=10)
st.pyplot(fig2)
plt.close(fig2)

# 6. Confusion Matrices
st.subheader("Confusion Matrices")

for model, name in [(best_lr, "Logistic Regression"), (best_svm, "SVM")]:
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
    disp.plot(cmap="Blues", ax=ax, colorbar=False)
    ax.set_title(f"Confusion Matrix - {name}")
    st.pyplot(fig)
    plt.close(fig)

# 7. Classification Reports

st.subheader("Classification Reports")

for model, name in [(best_lr, "Logistic Regression"), (best_svm, "SVM")]:
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=target_names, output_dict=True)
    st.write(f"**{name}**")
    st.dataframe(pd.DataFrame(report).transpose())

# 8. Best Model (Now Consistent)

st.subheader("🏆 Best Model")
if grid_svm.best_score_ >= grid_lr.best_score_:
    st.success(f"Best Model: **SVM** with CV accuracy {grid_svm.best_score_:.3f}")
else:
    st.success(f"Best Model: **Logistic Regression** with CV accuracy {grid_lr.best_score_:.3f}")
