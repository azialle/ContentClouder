import streamlit as st

def url_input():
    st.subheader("Youtube Link")
    with st.container(border=True):
        col1, col2 = st.columns([8, 2])

        with col1:
            url = st.text_input(
                "Paste your YouTube URL here:", 
                label_visibility="collapsed",
                placeholder="Paste your YouTube URL here..."
            )

        with col2:
            generate_btn = st.button("Generate", width="stretch")
        
    return url, generate_btn

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
    with st.container(border=True, height="stretch"):
        theme = st.selectbox(
            "Color Palette",
            options=["viridis", "plasma", "inferno", "magma", "cool", "spring"],
            placeholder="Choose a color",
            index=None,
        )

        shape = st.selectbox(
            "Shape Mask",
            options=["apple", "banana", "mango"],
            placeholder="Choose a shape",
            index=None,
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