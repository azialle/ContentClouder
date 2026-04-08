import streamlit as st
from styles.page_config import page_config
from components.url_input import render_url
from components.sidebar import sidebar
from components.cloud_display import display_word_cloud

page_config()

settings = sidebar()

url, generate_btn = render_url()

cloud_result = None

if generate_btn:
    if url:
        st.info(f"Processing video: {url}")
    else:
        st.error("Please enter a valid URL.")

display_word_cloud(cloud_result)