import streamlit as st

def render_url():
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