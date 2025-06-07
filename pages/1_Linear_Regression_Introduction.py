import streamlit as st
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from src import plot_linear_regression, load_markdown
from config import INTRO_PATH, EXPLAINER_PATH

intro_md = load_markdown(INTRO_PATH)
st.markdown(intro_md)                                             

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Here's a preview of your data:")
    st.write(df.head())

    # User choose columns
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_cols) >= 2:
        st.success(f"Found numeric columns: {numeric_cols}")
        x_col = st.selectbox("Select X column (input feature)", numeric_cols)
        y_col = st.selectbox("Select Y column (output/target)", numeric_cols, index=1)

        # Prepare data
        X = df[[x_col]]
        y = df[[y_col]]

        # Linear Regression
        model = LinearRegression()
        model.fit(X, y)
        prediction = model.predict(X)

        # Plot
        plot_linear_regression(X, y, prediction, x_col, y_col)

        # Show coefficients 
        slope = model.coef_.item()
        intercept = float(model.intercept_)
        
        coeff_text = f'''
        ### What did the computer learn?
        The computer found this **equation**:
        $$
        \\hat{{y}} = {slope:.3f} \\times {x_col} + {intercept:.3f}          
        $$
        where:
        - $\\hat{{y}}$ is the **predicted value**
        - {x_col} is your **input feature**
        - **{slope:.3f}** is the **slope (coefficient)** - it shows how much {y_col} changes when {x_col} increases by 1.
        - **{intercept:.3f}** is the **intercept** - the value of {y_col} when {x_col} is zero.
        '''
        st.markdown(coeff_text)

        # Show residuals
        residuals = y - prediction
        st.markdown("""
        ### Residuals: How good is the fit?
        The **residuals** (differences between actual and predicted) tell us how well the line fits the data.
        """)
        st.write(residuals.describe())
    else:
        st.warning("Please upload a dataset with at least 2 numeric columns.")
else:
    st.info("Upload a CSV file to get started!")


explainer_md = load_markdown(EXPLAINER_PATH)
st.markdown(explainer_md)



 