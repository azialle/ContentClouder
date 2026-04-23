from wordcloud import WordCloud, STOPWORDS
import io

class CloudVisualizer:
    def __init__(self, transcript, settings):
        self.transcript = transcript
        self.settings = settings

    def generate(self):
        if not self.transcript:
            return None
        
        theme = self.settings.get("theme", "viridis")
        bg = self.settings.get("background", "white").lower()
        max_words = self.settings.get("max_words", 100)
        
        stopwords = set(STOPWORDS)
        user_excluded = self.settings.get("exclude_words", "")
        if user_excluded:
            custom_words = [words.strip().lower() for words in user_excluded.replace(",", " ").split() if words.strip()]
            stopwords.update(custom_words)
        
        word_cloud = WordCloud(
            background_color=bg,
            max_words=max_words,
            colormap=theme,
            stopwords=stopwords,
            width=1600, 
            height=1000,
            prefer_horizontal=0.9,
            scale=1.5,
            random_state=42,
            mode="RGBA" if bg == "none" else "RGB"
        ).generate(self.transcript)

        img = word_cloud.to_image()
        img_bytes = io.BytesIO()
        img.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        
        return img_bytes
