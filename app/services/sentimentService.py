from textblob import TextBlob
from typing import Tuple


def analyze_sentiment_text(text: str) -> Tuple[str, float]:


    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity, 3)

    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, polarity
