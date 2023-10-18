"""Analyzing text retrieved per subject"""
import pandas as pd
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')  # Download the VADER lexicon

#variables setting - importing from local 

working_directory = "/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/"
file_name = "news_data_Israel_1697595469.csv"
file_pointer = f"{working_directory}{file_name}"
df = pd.read_csv(file_pointer)


#define function for cleanse of the text 
def clean_text(text):
    # Use regular expressions to keep only letters and whitespace
    my_stopwords = nltk.corpus.stopwords.words("english")
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    words = nltk.word_tokenize(cleaned_text)
    words_nstw = [word for word in words if word not in my_stopwords]
    #ideal to remove stopwords 
    return words_nstw

df['title_2'] = df['title'].apply(clean_text)
articles_list = df["title_2"].to_list()

#define function for text sentiment analysis
def analyze_sentiment(df):
    analyzer = SentimentIntensityAnalyzer()
    df["sentiment_text"] = df["title_2"].apply(lambda x: str(x).encode('utf-8'))
    df["sentiment_score_neg1"] = df["sentiment_text"].apply(lambda x: analyzer.polarity_scores(x.decode('utf-8'))['neg'])
    
    for index, row in df.iterrows():
        scores = analyzer.polarity_scores(row['sentiment_text'].decode('utf-8'))
        df.at[index, 'sentiment_score_neg2'] = scores['neg']
        df.at[index, 'sentiment_score_neu'] = scores['neu']
        df.at[index, 'sentiment_score_pos'] = scores['pos']
        df.at[index, 'sentiment_score_compound'] = scores['compound']

    return df

df_sentiment = analyze_sentiment(df)

print(df_sentiment.head(5))
print(df["sentiment_score_neg1"].mean())
print(df["sentiment_score_neg2"].mean())