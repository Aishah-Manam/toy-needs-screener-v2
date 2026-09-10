"""Wraps toy_screener.html inside a Streamlit page.

This does NOT re-implement the tool in Streamlit widgets — it just loads the
existing, already-tested HTML/JS file and renders it inside an iframe-like
component. The model, questions, and logic are identical to the standalone file.
"""
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title='Emotional Toy Needs Screener', page_icon='🧩', layout='wide')

html_path = Path(__file__).parent / 'toy_screener.html'
html_content = html_path.read_text(encoding='utf-8')

# Height is generous because the form (22 questions across 4 sections) plus
# results can run long. scrolling=True lets the user scroll within the frame
# if their screen is shorter than the content.
components.html(html_content, height=2400, scrolling=True)
