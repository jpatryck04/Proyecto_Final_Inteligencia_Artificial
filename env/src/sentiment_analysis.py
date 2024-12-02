from textblob import TextBlob

def analyze_sentiments(data):
    # Analizar sentimiento en las reseñas
    def analyze_sentiment(review):
        analysis = TextBlob(review)
        return analysis.sentiment.polarity  # Valor entre -1 (negativo) y 1 (positivo)

    data['sentiment'] = data['reviews'].apply(analyze_sentiment)
    return data

