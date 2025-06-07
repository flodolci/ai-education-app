import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd

from matplotlib.axes import Axes
from matplotlib.figure import Figure

def plot_linear_regression(X: pd.DataFrame, 
                           y: pd.DataFrame, 
                           prediction: np.ndarray, 
                           x_col: str, 
                           y_col: str) -> None:
    """
    Plots the linear regression fit using Streamlit. 

    Args:
        X (pd.DataFrame): Input features (1D or 2D).
        Y (pd.DataFrame): Actual target values.
        prediction (np.ndarray): Predicted target values from the regression model.
        x_col (str): Label for the X-axis.
        y_col (str): Label for the Y-axis. 
    """
    st.header("Linear Regression Fit")
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots()
    ax.scatter(X, y, label="Actual Data", color="blue", alpha=0.6)
    ax.plot(X, prediction, color="red", label="Regression Line", linewidth=2)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.legend()
    st.pyplot(fig)