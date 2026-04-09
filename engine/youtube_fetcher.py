from youtube_transcript_api import YouTubeTranscriptApi
import re
import yt_dlp
from datetime import datetime, timedelta

YT_ID_PATTERN = r"(?:v=|\/|be\/)([0-9A-Za-z_-]{11})"

class YoutubeFetcher:
    def __init__(self, url):
        self.url = url
        self.api = YouTubeTranscriptApi()
        self.video_id = self._extract_video_id()

    def _extract_video_id(self):
        match = re.search(YT_ID_PATTERN, self.url)
        return match.group(1) if match else None
    
    def video_thumbnail(self):
        if self.video_id:
            return f"https://img.youtube.com/vi/{self.video_id}/maxresdefault.jpg"
        return None
    
    def video_metadata(self):
        ydl_opts = {"quiet": True, "no_warnings": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.url, download=False)
            raw_date = info.get("upload_date")

            formatted_date = "N/A"
            if raw_date:
                formatted_date = datetime.strptime(raw_date, "%Y%m%d").strftime("%b %d, %Y")

            duration_seconds = info.get("duration", 0)
            time = timedelta(seconds=duration_seconds)
            formatted_duration = str(time)
            if formatted_duration.startswith("0:"):
                formatted_duration = formatted_duration[2:]

            metadata = {
                "title": info.get("title"),
                "published_date": formatted_date,
                "channel": info.get("uploader"),
                "duration": formatted_duration,
                "views": info.get("view_count")
            }
        return metadata

    def get_transcript(self):
        fetched_data = self.api.fetch(self.video_id)
        transcript_list = fetched_data.to_raw_data()

        transcript_texts = [transcript["text"] for transcript in transcript_list]
        return " ".join(transcript_texts)
