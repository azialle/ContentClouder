from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io

class CloudVisualizer:
    def __init__(self, transcript, settings):
        self.transcript = transcript
        self.theme = settings.get("theme", "viridis")
        self.background = settings.get("background", "#FFFFFF")
        self.max_words = settings.get("max_words", 200)

    def generate(self):
        if not self.transcript:
            return None
        
        word_cloud = WordCloud(
            background_color=self.background,
            max_words=self.max_words,
            colormap=self.theme,
            width=800,
            height=400,
            random_state=42,
            mode="RGBA" if self.background == "none" else "RGB"
        )

        cloud = word_cloud.generate(self.transcript)

        img_bytes = io.BytesIO()
        plt.figure(figsize=(10, 5))
        plt.imshow(cloud, interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout(pad=0)

        plt.savefig(img_bytes, format="png")
        img_bytes.seek(0)
        plt.close()
        
        return img_bytes