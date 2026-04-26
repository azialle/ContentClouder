import streamlit as st
import matplotlib.pyplot as plt
import os

def url_input():
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
    with st.container(border=True, width="stretch"):
        col1, col2 = st.columns([1, 1.5])
        with col1:
            st.image(thumbnail_url)
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
    with st.container(border=True, height=550, vertical_alignment="center"):
        if cloud_image is not None:
            st.image(cloud_image)

def _format_shape_name(name):
    if name == "None":
        return "Rectangle (Default)"
    return name.replace("_", " ").title()

def customize_panel(cloud_image=None):         
    all_colormaps = sorted(
        [cmap for cmap in plt.colormaps() if cmap not in {"prism", "prism_r"}],
        key=str.lower
    )
    IMG_DIR = os.path.join("assets", "img")
    
    if os.path.exists(IMG_DIR):
        svg_files = [file.replace(".svg", "") for file in os.listdir(IMG_DIR) if file.endswith(".svg")]
        svg_files.sort()
    else:
        svg_files = []

    shape_options = ["None"] + svg_files

    def format_cmap(name):
        is_reversed = name.endswith("_r")
        display_name = name[:-2] if is_reversed else name
        display_name = display_name.replace("_", " ")
        if display_name.islower():
            display_name = display_name.title()
        return f"{display_name} (Reversed)" if is_reversed else display_name
    
    with st.container(border=True, height=550):
        theme = st.selectbox(
            "Color Palette", 
            options=all_colormaps, 
            index=all_colormaps.index("viridis"),
            format_func=format_cmap,
            key="theme_selector"
        )

        shape = st.selectbox(
            "Shape Mask",
            options=shape_options,
            format_func=_format_shape_name,
            key="shape_selector"
        )

        bg_color = st.radio(
            "Background Color",
            options=["White", "Black"],
            horizontal=True,
            key="bg_selector"
        )

        max_words = st.number_input(
            "Max Words",
            min_value=10,
            max_value=250,
            value=100,
            step=10,
            key="words_selector"
        )

        exclude_words = st.text_area(
            label="Exclude Words",
            placeholder="Add words to exclude from the cloud...",
            height="stretch", 
            help="Enter words to exclude, separated by commas or new lines.",
            key="exclude_input"
        )

        if cloud_image is not None:
            st.download_button(
                label="Download Word Cloud",
                data=cloud_image, 
                file_name="content_cloud.png",
                mime="image/png",
                width="stretch"
            )

        settings = {
            "theme": theme,
            "shape": shape,
            "background": bg_color,
            "max_words": max_words,
            "exclude_words": exclude_words
        }
        
        return settings
