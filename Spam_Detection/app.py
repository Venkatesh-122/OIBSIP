
import streamlit as st
import joblib

# Load the model and vectorizer
model = joblib.load("spam_classifier_nb.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit UI
st.title("📧 Spam Classifier App")
st.write("Enter a message and find out if it’s Spam or Not Spam!")

# User input
user_input = st.text_area("Type your message here:")

if st.button("Predict"):
    if user_input.strip() != "":
        # Transform input using the same vectorizer
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)[0]

        if prediction == 1:
            st.error("🚨 This message is **Spam**!")
        else:
            st.success("✅ This message is **Not Spam**.")
    else:
        st.warning("⚠️ Please enter a message to classify.")
