import pandas as pd
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

file_path = "C:\Users\navee\Desktop\saturn_fe\instagram_comments_sample.csv"  # Update if the file is elsewhere
df = pd.read_csv(file_path)

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    if pd.isna(text):
        return "Neutral", 0  # Handle missing text

    # VADER Sentiment Analysis
    vader_score = sia.polarity_scores(text)["compound"]
    
    # TextBlob Sentiment Analysis
    textblob_score = TextBlob(text).sentiment.polarity
    
    # Final sentiment based on VADER score
    if vader_score >= 0.05:
        sentiment = "Positive"
    elif vader_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, vader_score

df["Sentiment"], df["Sentiment Score"] = zip(*df["Comment"].apply(analyze_sentiment))

# Save results to a new CSV file
output_file = "insta_comments.csv"
df.to_csv(output_file, index=False)

print(f"Sentiment analysis completed! Results saved to {output_file}")

sentiment_counts = df['Sentiment'].value_counts()
sentiment_counts

total_reviews = len(df)
sentiment_percentages = (sentiment_counts / total_reviews) * 100

print("Sentiment Counts:")
print(sentiment_counts)
print("\nSentiment Percentages:")
sentiment_percentages

# prompt: by calculating the scores give me an overall term if it is positive or negative or neutral with percentage 

import pandas as pd
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

file_path = "/content/amazon_sample.csv"  # Update if the file is elsewhere
df = pd.read_csv(file_path)

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    if pd.isna(text):
        return "Neutral", 0  # Handle missing text

    # VADER Sentiment Analysis
    vader_score = sia.polarity_scores(text)["compound"]
    
    # TextBlob Sentiment Analysis
    textblob_score = TextBlob(text).sentiment.polarity
    
    # Final sentiment based on VADER score
    if vader_score >= 0.05:
        sentiment = "Positive"
    elif vader_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, vader_score

df["Sentiment"], df["Sentiment Score"] = zip(*df["Review"].apply(analyze_sentiment))

# Calculate overall sentiment percentages
sentiment_counts = df['Sentiment'].value_counts()
total_reviews = len(df)
sentiment_percentages = (sentiment_counts / total_reviews) * 100

# Determine the overall sentiment
if sentiment_percentages['Positive'] > sentiment_percentages['Negative'] and sentiment_percentages['Positive'] > sentiment_percentages['Neutral']:
    overall_sentiment = "Positive"
elif sentiment_percentages['Negative'] > sentiment_percentages['Positive'] and sentiment_percentages['Negative'] > sentiment_percentages['Neutral']:
    overall_sentiment = "Negative"
else:
    overall_sentiment = "Neutral"

print("Sentiment Counts:")
print(sentiment_counts)
print("\nSentiment Percentages:")
print(sentiment_percentages)
print(f"\nOverall Sentiment: {overall_sentiment}")
