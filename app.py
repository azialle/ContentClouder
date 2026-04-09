import streamlit as st
from styles.page_config import page_config
from components.url_input import render_url
from components.sidebar import sidebar
from components.cloud_display import display_word_cloud
from components.video_preview import YTVideoPreview

page_config()
settings = sidebar()
url, generate_btn = render_url()

cloud_result = None

if url:
    video = YTVideoPreview(url)
    video.preview(generate_btn)
    
    if generate_btn:
        with st.spinner("Fetching transcript..."):
            transcript_data = video.get_transcript()
            
            if transcript_data:
                st.session_state["transcript"] = transcript_data
            else:
                st.error("No transcript found.")

    if "transcript" in st.session_state:
        with st.container(border=True):
            display_word_cloud(cloud_result)
else:
    if "transcript" in st.session_state:
        del st.session_state["transcript"]
    st.info("Paste a YouTube URL above to get started.")
