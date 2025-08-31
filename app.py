import streamlit as st
import numpy as np
import pickle
from sklearn.impute import SimpleImputer



model= pickle.load(open("model.pkl", "rb"))

st.title("💧 Water Potability Prediction")
st.write("Enter water quality parameters to check if the water is safe to drink.")

ph = st.number_input("pH (0-14)", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness (mg/L)", min_value=0.0, value=150.0)
solids = st.number_input("Solids (ppm)", min_value=0.0, value=10000.0)
chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, value=7.0)
sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, value=350.0)
conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, value=400.0)
organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, value=10.0)
trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, value=60.0)
turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, value=4.0)

features = np.array([[ph, hardness, solids, chloramines, sulfate,
                      conductivity, organic_carbon, trihalomethanes, turbidity]])

imputer = SimpleImputer(strategy='median')
features = imputer.fit_transform(features)
if st.button("Check Potability"):
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("✅ The water is **Potable (Safe to Drink)**")
    else:
        st.error("❌ The water is **Not Potable (Unsafe to Drink)**")
