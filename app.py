import streamlit as st
from styles.page_config import page_config
from components.display import url_input, cloud_viewer, customize_panel
from components.video_preview import YTVideoPreview
from engine.processor import TranscriptProcessor
from engine.visualizer import CloudVisualizer

@st.cache_data(show_spinner=False)
def get_cloud_image(transcript, settings_items):
    visualizer = CloudVisualizer(transcript, dict(settings_items))
    return visualizer.generate()

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
    
            current_settings = {
                "theme": st.session_state.get("theme_selector", "viridis"),
                "background": st.session_state.get("bg_selector", "White"),
                "max_words": st.session_state.get("words_selector", 100),
                "exclude_words": st.session_state.get("exclude_input", ""),
                "shape": st.session_state.get("shape_selector", "None")
            }

            st.session_state["cloud_img_data"] = get_cloud_image(
                st.session_state["transcript"], 
                tuple(current_settings.items())
            )

            col1, col2 = st.columns([7, 3]) 
            with col2:
                customize_panel(cloud_image=st.session_state["cloud_img_data"])
            with col1:
                cloud_viewer(st.session_state["cloud_img_data"])

    if not url:
        st.session_state.update({
            "transcript": None,
            "video_info": None,
            "cloud_img_data": None,
            "last_settings": None 
        })