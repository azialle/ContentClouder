import streamlit as st
import matplotlib.pyplot as plt

def url_input():
    st.subheader("Youtube Link", text_alignment="center")
    with st.container(border=True):
        col1, col2 = st.columns([3, 1], vertical_alignment="center")
        
    with col1:
        url = st.text_input(
            "Paste your YouTube URL here:", 
            label_visibility="collapsed",
            placeholder="Paste your YouTube URL here..."
        )

    with col2:
        generate_btn = st.button("Generate", width="stretch")
    
    return url, generate_btn


def video_preview(thumbnail_url, metadata):
        st.subheader("Video Preview", text_alignment="center")
        left_gap, center_col, right_gap = st.columns([1, 5, 1])
        with center_col:
            with st.container(border=True, width="stretch"):
                col1, col2 = st.columns(2)
            with col1:
                st.image(thumbnail_url, width="stretch")
            with col2:
                if metadata:
                    st.markdown(f"""
                    <div class="preview-text-column">
                        <div class="preview-title">{metadata["title"]}</div>
                        <div class="preview-metadata">
                            <b>Channel:</b> {metadata["channel"]} <br>
                            <b>Duration:</b> {metadata["duration"]} <br>
                            <b>Views:</b> {metadata["views"]:,} views <br>
                            <b>Published:</b> {metadata["published_date"]}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                else:
                    st.warning("Metadata unavailable for this video.")


def cloud_viewer(cloud_image=None):
    st.subheader("Word Cloud Visualization")
    with st.container(border=True):
        if cloud_image is not None:
            st.image(cloud_image, width="stretch")
            
            st.download_button(
                label="💾 Download Word Cloud",
                data=b"", 
                file_name="content_cloud.png",
                mime="image/png",
                width="stretch"
            )
        else:
            st.markdown(
                """
                <div class="word-cloud-placeholder">
                    Your word cloud will appear here.
                </div>
                """, 
                unsafe_allow_html=True
            )


def customize_panel():         
    st.subheader("Customization")
    all_colormaps = plt.colormaps()
    
    with st.container(border=True, height="stretch"):
        theme = st.selectbox(
            "Color Palette", 
            options=all_colormaps, 
            index=all_colormaps.index("viridis")
        )

        shape = st.selectbox(
            "Shape Mask",
            options=["apple", "banana", "mango"],
        )

        bg_color = st.radio(
            "Background Color",
            options=["White", "Black"],
            horizontal=True
        )

        max_words = st.slider(
            "Max Words",
            min_value=10,
            max_value=500,
            value=200,
            step=10
        )

        settings = {
            "theme": theme,
            "shape": shape,
            "background": bg_color,
            "max_words": max_words
        }
        
        return settings