import streamlit as st
from styles.page_config import page_config
from components.display import url_input, main_dashboard
from components.empty_state import show_feature_highlights
from components.video_preview import YTVideoPreview
from engine.processor import TranscriptProcessor
from engine.visualizer import CloudVisualizer
                
@st.cache_data(show_spinner=False)
def get_cloud_image(transcript, settings_items):
    visualizer = CloudVisualizer(transcript, dict(settings_items))
    return visualizer.generate()

@st.cache_data(show_spinner=False)
def get_filtered_transcript(transcript, settings_items):
    visualizer = CloudVisualizer(transcript, dict(settings_items))
    return visualizer.get_filtered_data()

page_config()

for key in ["cloud_img_data", "transcript", "video_info"]:
    if key not in st.session_state: st.session_state[key] = None

with st.container(): 
    _, center_col, _ = st.columns([1, 5, 1])
    with center_col:
        url, generate_btn = url_input()
        
        if not url:
            st.session_state.update({"transcript": None, "video_info": None, "cloud_img_data": None})

        if generate_btn and url:
            video = YTVideoPreview(url)
            with st.spinner("Processing..."):
                transcript_data = video.transcript()
                if transcript_data:
                    st.session_state.update({
                        "transcript": TranscriptProcessor(transcript_data).clean(),
                        "video_info": video,
                        "exclude_input": ""
                    })
                else:
                    st.error("No transcript found.")

        if st.session_state["video_info"]:
            st.session_state["video_info"].show()
            
            st.session_state["cloud_img_data"], _ = main_dashboard(
                st.session_state["transcript"], 
                st.session_state["cloud_img_data"],
                get_cloud_image,
                get_filtered_transcript
            )
        else:
            show_feature_highlights()
