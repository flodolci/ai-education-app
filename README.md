# AI Explorers Playground: Linear Regression Web App

Welcome to the **AI Explorers Playground**! This web app is a simple, interactive tool that demonstrates how **Linear Regression** works in practice. 
It allows you to upload your own dataset (CSV) and see how a linear regression model fits the data, complete with a step-by-step explanation and a visual plot.

For now, only linear regression is implemented, but further models and interactive explanations will be added in the future. The goal is to provide an engaging 
and educational experience to help you understand the fundamentals of machine learning.

---

## Features

- Upload your own CSV file to apply linear regression.
- Step-by-step explanation of the linear regression mathematics.
- Visual plot of the fitted model.
- Preloaded sample dataset if you don’t have your own CSV.
- Future updates will include:
  - Additional regression and classification models.
  - Interactive explanations and visualizations.
  - Enhanced analysis options.
  - ... and much more!
---

## Getting Started Locally

Follow these steps to download and run the app on your local machine:

1. **Clone the repository**

```bash
git clone git@github.com:flodolci/ai-education-app.git
cd ai-explorers-linear-regression
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate  
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run app.py
```

## Usage

- Visit the local Streamlit link provided (typically http://localhost:8501).
- Upload your CSV file or use the default dataset provided in the data folder.
- The app will display the linear regression fit and a mathematical explanation of the model at the end.

## Deployment

The app is already deployed on Streamlit Community Cloud and can be accessed directly at: https://dolci-ai.streamlit.app

You can also deploy it on:

- Streamlit Community Cloud (free for public projects)
- Hosting services like Heroku, AWS, Azure, or any cloud platform of your choice.

## Contributing

Contributions and feedback are welcome! Please open an issue or submit a pull request to share your ideas and improvements.

Enjoy exploring linear regression and stay tuned for future updates and models!