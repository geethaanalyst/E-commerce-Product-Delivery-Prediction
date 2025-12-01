import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and feature names
clf = joblib.load('rf_model.joblib')
feature_names = joblib.load('feature_names.joblib')

# Define categorical options (must match label encoding order used in training)
warehouse_blocks = ['A', 'B', 'C', 'D', 'F']
mode_of_shipment = ['Flight', 'Ship', 'Road']
product_importance = ['low', 'medium', 'high']
gender = ['F', 'M']

st.title('E-commerce Product Delivery Prediction App')

# User input form
with st.form('input_form'):
    Warehouse_block = st.selectbox('Warehouse Block', warehouse_blocks)
    Mode_of_Shipment = st.selectbox('Mode of Shipment', mode_of_shipment)
    Customer_care_calls = st.number_input('Customer Care Calls', min_value=1, max_value=10, value=3)
    Customer_rating = st.slider('Customer Rating', min_value=1, max_value=5, value=3)
    Cost_of_the_Product = st.number_input('Cost of the Product', min_value=50, max_value=300, value=150)
    Prior_purchases = st.number_input('Prior Purchases', min_value=1, max_value=10, value=3)
    Product_importance = st.selectbox('Product Importance', product_importance)
    Gender = st.selectbox('Gender', gender)
    Discount_offered = st.number_input('Discount Offered', min_value=0, max_value=65, value=10)
    Weight_in_gms = st.number_input('Weight in grams', min_value=50, max_value=8000, value=2000)
    submit = st.form_submit_button('Predict')

# Manual encoding (must match LabelEncoder order in training script)
def manual_encode(val, options):
    return options.index(val)

if submit:
    input_data = [
        manual_encode(Warehouse_block, warehouse_blocks),
        manual_encode(Mode_of_Shipment, mode_of_shipment),
        Customer_care_calls,
        Customer_rating,
        Cost_of_the_Product,
        Prior_purchases,
        manual_encode(Product_importance, product_importance),
        manual_encode(Gender, gender),
        Discount_offered,
        Weight_in_gms
    ]
    input_df = pd.DataFrame([input_data], columns=feature_names)
    prediction = clf.predict(input_df)[0]
    st.write('### Prediction:')
    if prediction == 0:
        st.success('The shipment is likely to reach on time.')
    else:
        st.error('The shipment is likely to be delayed.')