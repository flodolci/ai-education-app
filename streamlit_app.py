import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Explorers: Linear Regression", layout="wide")
st.title("AI Explorers: Linear Regression Playground")

st.markdown("""
Welcome to the **AI Explorers** playground!
Today, we'll explore how **Linear Regression** works and learn its mathematics step by step.
""")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Here's a preview of your data:")
    st.write(df.head())

    