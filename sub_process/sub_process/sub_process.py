"""Analyzing text retrieved per subject"""
import pandas as pd
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#variables setting - importing from local 

working_directory = "/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/"
file_name = "news_data_Cosmos_1697590124.csv"
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

print(unique_list)
