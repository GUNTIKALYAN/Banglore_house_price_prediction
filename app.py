import streamlit as st
from server import util
# Load model and data once
util.load_saved_artifacts()

# price = util.get_estimated_price("1st Phase JP Nagar",1000,3,3)
# st.write(f"Predicted price : Rs{price} Lakhs")

# App title
st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")
st.title("🏠 Bangalore House Price Prediction")
st.markdown("Estimate the price of a house based on location, size, BHK, and bathrooms.")

# Inputs
location = st.selectbox("Select Location", util.get_location_names())
sqft = st.number_input("Total Square Feet Area", min_value=500, max_value=10000, step=10)
bhk = st.number_input("Number of Bedrooms (BHK)", min_value=1, max_value=10, step=1)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)

# Prediction
if st.button("Predict Price"):
    estimated_price = util.get_estimated_price(location, sqft, bhk, bath)
    st.success(f"🏷️ Estimated Price: ₹ {estimated_price} Lakhs")
