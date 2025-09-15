import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load pipeline (with preprocessing included)
# Corrected path to load the pipeline
model = joblib.load("artifacts/best_xgb_model.joblib")

st.set_page_config(page_title="Car Price Prediction", layout="centered")

st.title("🚗 Car Price Prediction App")
st.write("Enter the details of the car to predict its selling price.")

# Inputs
present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, max_value=50.0, step=0.1)
kms_driven = st.number_input("Driven Kms", min_value=0, max_value=500000, step=500)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
selling_type = st.selectbox("Selling Type", ["Dealer", "Individual"]) # Corrected column name
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
# Removed Owner input as it was dropped during preprocessing
car_age = st.slider("Car Age (Years)", 0, 20, 5)

# Predict
if st.button("Predict Price"):
    # Create input data with correct column names and transformations
    input_data = pd.DataFrame({
        "Present_Price": [present_price],
        # Apply log1p transformation to Driven_kms before passing to the pipeline
        "Driven_kms": [np.log1p(kms_driven)],
        "Fuel_Type": [fuel_type],
        "Selling_type": [selling_type], # Corrected column name
        "Transmission": [transmission],
        "Car_Age": [car_age]
    })

    # The pipeline handles all preprocessing and prediction
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Selling Price: {prediction:.2f} lakhs")
