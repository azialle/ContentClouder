import streamlit as st
import os

def page_config():
    st.set_page_config(page_title="ContentClouder", page_icon="☁️", layout="wide")
    css_path = os.path.join("styles", "style.css")
    if os.path.exists(css_path):
        with open(css_path) as file:
            st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

    st.markdown("""
        <div class="title-container">
            <span class="title-accent">Content</span><span class="title-main">Clouder</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p class="app-description">
            Generate Wordcloud from Youtube Videos
        </p>
        """, 
        unsafe_allow_html=True
    )