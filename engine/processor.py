import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from langdetect import detect, DetectorFactory
import re
import os

nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

nltk.data.path.append(nltk_data_path)

nltk.download("punkt_tab", download_dir=nltk_data_path, quiet=True)
nltk.download("punkt", download_dir=nltk_data_path, quiet=True)
nltk.download("averaged_perceptron_tagger_eng", download_dir=nltk_data_path, quiet=True)
nltk.download("stopwords", download_dir=nltk_data_path, quiet=True)

DetectorFactory.seed = 0

class TranscriptProcessor:
    def __init__(self, transcript):
        self.transcript = transcript
        try:
            self.language_code = detect(transcript)
        except:
            self.language_code = "en"

    def _get_stopwords(self):
        nltk_languages = stopwords.fileids()
        detected_code = self.language_code
        language = next(
        (language for language in nltk_languages if language.startswith(detected_code)), 
        "english"
    )
        try:
            stops = set(stopwords.words(language))
        except:
            stops = set(stopwords.words("english"))

        return stops

    def clean(self):
        if not self.transcript:
            return ""
        
        text = self.transcript.lower()
        text = re.sub(r"\[.*?\]", "", text)

        words = word_tokenize(text)
        stop_words = self._get_stopwords()
        tagged_words = nltk.pos_tag(words, lang="eng")

        cleaned_list = []
        for word, tag in tagged_words:
            is_correct_tag = tag in ("NN", "NNS", "JJ", "JJR", "JJS")
            is_not_stopword = word not in stop_words
            is_valid_format = word.isalpha() and len(word) > 2

            if is_correct_tag and is_not_stopword and is_valid_format:
                cleaned_list.append(word)
        
        if cleaned_list:
            fdist = FreqDist(cleaned_list)
            most_common_noise = {word for word, _ in fdist.most_common(3)}
            final_list = [word for word in cleaned_list if word not in most_common_noise]
            return " ".join(final_list)
        
        return ""
        
