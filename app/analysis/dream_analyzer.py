import spacy
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER if missing
nltk.download("vader_lexicon", quiet=True)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
sid = SentimentIntensityAnalyzer()

def analyze_dream(text: str):
    doc = nlp(text)

    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    verbs = [token.text for token in doc if token.pos_ == "VERB"]

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    vader_score = sid.polarity_scores(text)

    return {
        "nouns": list(set(nouns)),
        "adjectives": list(set(adjectives)),
        "verbs": list(set(verbs)),
        "polarity": polarity,
        "subjectivity": subjectivity,
        "emotion_score": vader_score,
    }
