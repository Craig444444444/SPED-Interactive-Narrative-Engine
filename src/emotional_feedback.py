from textblob import TextBlob

def analyze_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    elif "anger" in text.lower() or "rage" in text.lower():
        return "angry"
    else:
        return "neutral"
