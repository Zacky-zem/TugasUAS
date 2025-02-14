from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analisis sentimen menggunakan TextBlob.
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"
