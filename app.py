import streamlit as st
from styles.page_config import page_config
from components.display import url_input, cloud_viewer, customize_panel
from components.video_preview import YTVideoPreview
from engine.processor import TranscriptProcessor

page_config()

left_gap, center_col, right_gap = st.columns([1, 5, 1])

with center_col:
    url, generate_btn = url_input()
    if generate_btn and url:
        video = YTVideoPreview(url)
        with st.spinner("Fetching transcript..."):
            transcript_data = video.transcript()
            if transcript_data:
                processor = TranscriptProcessor(transcript_data)
                st.session_state["transcript"] = processor.clean()
                st.session_state["video_info"] = video
            else:
                st.error("No transcript found.")
            
    if "video_info" in st.session_state:
        st.session_state["video_info"].show()
        
        st.divider()
        
        col1, col2 = st.columns([7, 3]) 
        with col1:
            cloud_viewer() 
        with col2:
            settings = customize_panel()

    if not url:
        st.session_state.pop("transcript", None)
        st.session_state.pop("video_info", None)