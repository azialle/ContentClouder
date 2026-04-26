from wordcloud import WordCloud, STOPWORDS
import io
import numpy as np
import os
import xml.etree.ElementTree as ET
from svgpath2mpl import parse_path


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
        shape_name = self.settings.get("shape", None)
      
        CANVAS_WIDTH = 1600
        CANVAS_HEIGHT = 1000
        mask_array = None
        
        if shape_name != "None":
            svg_path = f"assets/img/{shape_name}.svg"
            if os.path.exists(svg_path):
                try:
                    tree = ET.parse(svg_path)
                    root = tree.getroot()
                    
                    paths = root.findall(".//{http://www.w3.org/2000/svg}path")
                    if not paths:
                        paths = root.findall(".//path")
                    
                    if paths:
                        combined_d = " ".join([path.get("d", "") for path in paths])
                        mpl_path = parse_path(combined_d)
                        
                        extents = mpl_path.get_extents()
                        padding = 150
                        
                        scale = min((CANVAS_WIDTH - padding) / extents.width, 
                                    (CANVAS_HEIGHT - padding) / extents.height)
                        
                        verts = mpl_path.vertices
                        verts = verts - [extents.x0, extents.y0]
                        verts = verts * scale
                        
                        offset_x = (CANVAS_WIDTH - (extents.width * scale)) / 2
                        offset_y = (CANVAS_HEIGHT - (extents.height * scale)) / 2
                        verts = verts + [offset_x, offset_y]
                        
                        mpl_path.vertices = verts
                        
                        y, x = np.mgrid[:CANVAS_HEIGHT, :CANVAS_WIDTH]
                        points = np.column_stack((x.ravel(), y.ravel()))
                        mask_bool = mpl_path.contains_points(points).reshape(CANVAS_HEIGHT, CANVAS_WIDTH)
                    
                        mask_array = np.full((CANVAS_HEIGHT, CANVAS_WIDTH), 255, dtype=np.uint8)
                        mask_array[mask_bool] = 0
                except Exception as e:
                    print(f"Error processing SVG mask: {e}")
                    mask_array = None

        stopwords = set(STOPWORDS)
        user_excluded = self.settings.get("exclude_words", "")
        if user_excluded:
            custom_words = [words.strip().lower() for words in user_excluded.replace(",", " ").split() if words.strip()]
            stopwords.update(custom_words)
        
        filtered_freqs = {word: count for word, count in self.transcript.items() if word not in stopwords}
        
        def get_sort_priority(item):
             word, count = item
             return (-count, word)

        sorted_words = sorted(filtered_freqs.items(), key=get_sort_priority)
        top_freqs = dict(sorted_words[:max_words])

        word_cloud = WordCloud(
            background_color=bg,
            max_words=max_words,
            colormap=theme,
            mask=mask_array,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            margin=2,
            min_font_size=12,    
            max_font_size=200,
            prefer_horizontal=0.85,
            scale=1.5,
            random_state=42,
            mode="RGBA" if bg == "none" else "RGB"
        ).generate_from_frequencies(top_freqs)

        img = word_cloud.to_image()

        img_bytes = io.BytesIO()
        img.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        
        return img_bytes