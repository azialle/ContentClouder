from engine.youtube_fetcher import YoutubeFetcher
from components.display import video_preview

class YTVideoPreview(YoutubeFetcher):
    def __init__(self, url):
        super().__init__(url)

    def show(self):
        thumbnail_url = self.thumbnail()
        metadata = self.metadata()

        if thumbnail_url:
            video_preview(thumbnail_url, metadata)