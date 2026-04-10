import streamlit as st
from styles.page_config import page_config
from components.display import url_input, cloud_viewer, customize_panel
from components.video_preview import YTVideoPreview

page_config()
url, generate_btn = url_input()

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
else:
    if "transcript" in st.session_state:
        del st.session_state["transcript"]

col1, col2 = st.columns([7, 3]) 
with col1:
    cloud_viewer() 
with col2:
    settings = customize_panel()

