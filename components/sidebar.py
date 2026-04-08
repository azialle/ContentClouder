import streamlit as st

def sidebar():
    with st.sidebar:
        st.header("Word Cloud Customization")
        st.subheader("Settings")

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