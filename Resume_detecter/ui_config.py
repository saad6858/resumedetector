# =============================================================================
# ui_config.py — Streamlit Page Config & Branding Removal
# MUST be imported FIRST in app.py before any other imports
# =============================================================================

import streamlit as st

# =========================================================
# Page Configuration — MUST be the first Streamlit API call
# =========================================================
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# =========================================================
# MAXIMUM Streamlit Cloud Branding Removal CSS
# Targets every known injection point. Zero conflict with
# Sir Shan's .main / .title / .subtitle / .box classes.
# =========================================================
_HIDE_STREAMLIT_BRANDING = """
<style>
    /* 1. Hamburger menu (MainMenu) */
    #MainMenu {visibility: hidden !important;}

    /* 2. Footer — "Hosted with Streamlit" text + container */
    footer {display: none !important;}
    .stApp > footer {display: none !important;}
    [data-testid="stFooter"] {display: none !important;}

    /* 3. Top header bar */
    header {display: none !important;}
    .stApp > header {display: none !important;}

    /* 4. Deploy / Fork button */
    .stDeployButton {display: none !important;}
    [data-testid="stDeployButton"] {display: none !important;}

    /* 5. Top-right toolbar */
    [data-testid="stToolbar"] {display: none !important;}

    /* 6. Decoration / Crown logo */
    [data-testid="stDecoration"] {display: none !important;}
    .stDecoration {display: none !important;}

    /* 7. Streamlit logo images */
    img[alt*="Streamlit"] {display: none !important;}
    img[alt*="streamlit"] {display: none !important;}
    img[src*="streamlit"] {display: none !important;}

    /* 8. Streamlit links */
    a[href*="streamlit.io"] {display: none !important;}

    /* 9. Remove bottom padding where footer used to sit */
    .stApp {padding-bottom: 0 !important;}
</style>
"""
st.markdown(_HIDE_STREAMLIT_BRANDING, unsafe_allow_html=True)
