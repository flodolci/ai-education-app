# config.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
TEXTS_DIR = BASE_DIR / "texts"

TITLE_TEXT_PATH = TEXTS_DIR / "introduction.md"

CSS_PATH = ASSETS_DIR / "style.css"
INTRO_PATH = TEXTS_DIR / "linear_regression_intro.md"
EXPLAINER_PATH = TEXTS_DIR / "linear_regression_explainer.md"
COEFF_PATH = TEXTS_DIR / "linear_regression_coeffs.md"
IMAGE_PATH = ASSETS_DIR / "welcome.png"

