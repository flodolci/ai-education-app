import streamlit as st

from src import load_css, display_image, load_markdown
from config import CSS_PATH, IMAGE_PATH, TITLE_TEXT_PATH

st.set_page_config(page_title="AI ExplorersNo", layout="centered")
load_css(CSS_PATH)

st.title("Welcome to AI Explorers!")
st.write('''
This app is designed to provide an interactive and educational exploration of key machine learning concepts. 
Whether you're new to data science or want to deepen your understanding, you'll find intuitive explanations,
visualizations, and hands-on examples.     
''')

st.subheader("Topics You'll Explore")
title_text = load_markdown(TITLE_TEXT_PATH)
st.write(title_text)