# =============================================================================
# ui_config.py — UI Branding Removal
# MUST be imported BEFORE any other Streamlit calls in app.py
# =============================================================================

import streamlit as st

# ⭐⭐⭐⭐⭐ EXACT replica of Sir Shan's set_page_config + menu_items=None added
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    menu_items=None  # Only addition: hides hamburger menu
)

# ⭐⭐⭐⭐⭐ CSS to kill Streamlit Cloud branding ONLY
# Does NOT change layout, colors, fonts, or any visual element Sir Shan designed
_HIDE_BRANDING = """
<style>
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
</style>
"""
st.markdown(_HIDE_BRANDING, unsafe_allow_html=True)
