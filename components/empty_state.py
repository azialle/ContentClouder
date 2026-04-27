import streamlit as st

def show_feature_highlights():
    st.markdown('<p class="how-it-works-header">How it works</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, border=True)

    with col1:
        st.markdown("""
            <div class="feature-container">
                <div class="feature-icon">🔗</div>
                <div class="feature-title">Extract</div>
                <div class="feature-desc">
                    Paste a YouTube URL to retrieve the transcript and begin your analysis.
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="feature-container">
                <div class="feature-icon">☁️</div>
                <div class="feature-title">Visualize</div>
                <div class="feature-desc">
                    Generate a high-resolution word cloud highlighting key topics of the video.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="feature-container">
                <div class="feature-icon">🪄</div>
                <div class="feature-title">Refine</div>
                <div class="feature-desc">
                    Customize themes, shapes, and filter keywords to visualize exactly what you need.
                </div>
            </div>
        """, unsafe_allow_html=True)

  