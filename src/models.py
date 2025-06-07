from typing import Optional
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from src.plotting import plot_linear_regression


class LinearRegressionModel:
    """
    A class to handle linear regression tasks, from data selection to plotting.
    """

    def __init__(self, df: pd.DataFrame) -> None:
        self.df: pd.DataFrame = df
        self.numeric_cols: list[str] = df.select_dtypes(include=np.number).columns.tolist()
        self.model: LinearRegression = LinearRegression()
        self.X: Optional[pd.DataFrame] = None
        self.y: Optional[pd.DataFrame] = None
        self.prediction: Optional[np.ndarray] = None
        self.x_col: Optional[str] = None
        self.y_col: Optional[str] = None

    def select_features(self) -> bool:
        """
        Prompt user to select numeric input and output columns.

        Returns:
            bool: True if valid columns were selected, False otherwise.
        """
        if len(self.numeric_cols) < 2:
            st.warning("Please upload a dataset with at least 2 numeric columns.")
            return False

        st.success(f"Found numeric columns: {self.numeric_cols}")
        self.x_col = st.selectbox("Select X column (input feature)", self.numeric_cols)
        self.y_col = st.selectbox("Select Y column (output/target)", self.numeric_cols, index=1)

        self.X = self.df[[self.x_col]]
        self.y = self.df[[self.y_col]]
        return True

    def train_model(self) -> None:
        """
        Train the linear regression model and make predictions.
        """
        if self.X is not None and self.y is not None:
            self.model.fit(self.X, self.y)
            self.prediction = self.model.predict(self.X)
        else:
            st.error("Input and output features not set. Please select valid columns first.")

    def display_results(self) -> None:
        """
        Display the regression line, coefficients, and residuals.
        """
        if self.X is None or self.y is None or self.prediction is None:
            st.error("Model is not trained or data not selected.")
            return

        # Explicitly check that x_col and y_col are not None
        if self.x_col is None or self.y_col is None:
            st.error("Input and output columns are not set.")
            return

        # Plot regression fit
        plot_linear_regression(self.X, self.y, self.prediction, self.x_col, self.y_col)

        # Show coefficients
        slope: float = float(self.model.coef_.item())
        intercept: float = float(self.model.intercept_)

        coeff_text: str = f'''
        ### What did the computer learn?
        The computer found this **equation**:
        $$
        \\hat{{y}} = {slope:.3f} \\times {self.x_col} + {intercept:.3f}          
        $$
        where:
        - $\\hat{{y}}$ is the **predicted value**
        - {self.x_col} is your **input feature**
        - **{slope:.3f}** is the **slope (coefficient)** - it shows how much {self.y_col} changes when {self.x_col} increases by 1.
        - **{intercept:.3f}** is the **intercept** - the value of {self.y_col} when {self.x_col} is zero.
        '''
        st.markdown(coeff_text)

        # Show residuals
        residuals: pd.DataFrame = self.y - self.prediction
        st.markdown("""
        ### Residuals: How good is the fit?
        The **residuals** (differences between actual and predicted) tell us how well the line fits the data.
        """)
        st.write(residuals.describe())

