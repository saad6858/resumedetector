# =============================================================================
# ui_config.py — UI Branding Removal & Page Config
# Place this file in repo root. Add ONE line to top of app.py: import ui_config
# =============================================================================

import streamlit as st

# ⭐⭐⭐⭐⭐ PAGE CONFIG — must be FIRST Streamlit call
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered",
    menu_items=None  # Hides hamburger menu (Rerun, Settings, Print)
)

# ⭐⭐⭐⭐⭐ CSS INJECTION — kills footer, header, deploy button, toolbar
_HIDE_BRANDING = """
<style>
    /* Hide hamburger menu completely */
    #MainMenu {visibility: hidden !important;}
    
    /* Hide Streamlit footer ("Created by Streamlit", "Hosted with Streamlit") */
    footer {visibility: hidden !important;}
    
    /* Hide top header bar */
    header {visibility: hidden !important;}
    
    /* Hide "Fork" / "Deploy" button */
    .stDeployButton {display: none !important;}
    
    /* Hide top-right toolbar */
    [data-testid="stToolbar"] {display: none !important;}
    
    /* Hide GitHub icon in top-right */
    [data-testid="stDecoration"] {display: none !important;}
</style>
"""
st.markdown(_HIDE_BRANDING, unsafe_allow_html=True)