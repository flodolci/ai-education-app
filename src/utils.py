from pathlib import Path

import streamlit as st

def display_image(file_path: Path, width=200) -> None:
    """Display an image provided a given path."""
    try:
        if file_path.exists():
            st.image(str(file_path), width=width)
    except FileNotFoundError:
        st.warning(f"Image not found: {file_path}")
    except Exception as e:
        st.error(f"Error loading image: {e}")


def load_css(file_path: Path) -> None:
    """Load and inject CSS into the Streamlit app."""
    try:
        with file_path.open("r", encoding="utf-8") as f:
            css_content = f.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file not found: {file_path}")
    except Exception as e:
        st.error(f"Error loading CSS: {e}")


def load_markdown(file_path: Path) -> str:
    """Load markdown text from a file."""
    try:
        with file_path.open("r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        st.warning(f"Markdown file not found: {file_path}")
        return ""
    except Exception as e:
        st.error(f"Error loading markdown: {e}")
        return ""