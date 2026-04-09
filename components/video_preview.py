from engine.youtube_fetcher import YoutubeFetcher
import streamlit as st

class YTVideoPreview(YoutubeFetcher):
    def __init__(self, url):
        super().__init__(url)

    def preview(self, generate_btn):
        thumbnail_url = self.video_thumbnail()

        if thumbnail_url and not generate_btn:
            st.subheader("Video Preview")
            with st.container(border=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.image(thumbnail_url, width="stretch", link=self.url)
                with col2:
                    metadata = self.video_metadata()
                    if metadata:
                        st.subheader(metadata["title"])
                        st.write(f"**Channel:** {metadata["channel"]}")
                        st.write(f"**Published Date**: {metadata["published_date"]}")
                        st.write(f"**Duration:** {metadata["duration"]}")
                        st.write(f"**Views**: {metadata["views"]}")
                    else:
                        st.warning("Metadata unavailable for this video.")