from engine.youtube_fetcher import YoutubeFetcher
import streamlit as st

class YTVideoPreview(YoutubeFetcher):
    def __init__(self, url):
        super().__init__(url)

    def preview(self, generate_btn):
        thumbnail_url = self.video_thumbnail()
        metadata = self.video_metadata()

        if thumbnail_url and not generate_btn:
            st.subheader("Video Preview", text_alignment="center")
            left_gap, center_col, right_gap = st.columns([1, 5, 1])
            with center_col:
                with st.container(border=True, width="stretch"):
                    col1, col2 = st.columns([1, 1.5], gap="medium")
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