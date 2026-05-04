import streamlit as st
import numpy as np

st.set_page_config(page_title="AI Sales Predictor", layout="centered")

st.title("🤖 AI Sales Predictor")
st.write("Enter product details to predict sales")

# Inputs
price = st.number_input("Product Price", min_value=0.0)
marketing = st.number_input("Marketing Spend", min_value=0.0)
season = st.selectbox("Season", ["Low", "Medium", "High"])

# Convert season to number
season_map = {"Low": 1, "Medium": 2, "High": 3}
season_val = season_map[season]

# Fake AI model (simple formula)
def predict(price, marketing, season):
    return price * 0.3 + marketing * 0.5 + season * 100

if st.button("Predict Sales"):
    result = predict(price, marketing, season_val)
    st.success(f"📊 Predicted Sales: {result:.2f}")
