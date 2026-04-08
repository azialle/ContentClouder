import streamlit as st

def display_word_cloud(cloud_image=None):
    with st.container(border=True):
        if cloud_image is not None:
            st.image(cloud_image, width="stretch")
            
            st.download_button(
                label="💾 Download Word Cloud",
                data=b"", 
                file_name="content_cloud.png",
                mime="image/png"
            )
        else:
            st.info("Your word cloud will appear here once you click 'Generate'.")