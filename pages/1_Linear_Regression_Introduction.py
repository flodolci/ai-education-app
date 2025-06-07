import streamlit as st
import pandas as pd
import numpy as np

from src import LinearRegressionModel 
from src import plot_linear_regression, load_markdown
from config import INTRO_PATH, EXPLAINER_PATH

intro_md = load_markdown(INTRO_PATH)
st.markdown(intro_md)                                             

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Here's a preview of your data:")
    st.write(df.head())
    
    lin_reg = LinearRegressionModel(df)
    if lin_reg.select_features():
        lin_reg.train_model()
        lin_reg.display_results()
else:
    st.info("Upload a CSV file to get started!")

explainer_md = load_markdown(EXPLAINER_PATH)
st.markdown(explainer_md)



 