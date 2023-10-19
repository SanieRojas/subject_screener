"""Analyzing text retrieved per subject"""
import pandas as pd
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import pos_tag, ne_chunk

nltk.download(['stopwords', 'vader_lexicon', 'punkt']) 
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('x')


#variables setting - importing from local 
def file_to_df(user_folder, user_file):
    user_folder = input("Please introduce URL to working folder: ->  ")
    user_file = input("Please enter file name: ->  ")
    file_pointer = f"{user_folder}{user_file}"
    df = pd.read_csv(file_pointer)
    return df


#define function for cleanse of the text 
def clean_text(text):
    # Use regular expressions to keep only letters and whitespace
    my_stopwords = nltk.corpus.stopwords.words("english")
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    words = nltk.word_tokenize(cleaned_text)
    words_nstw = [word for word in words if word not in my_stopwords]
    return words_nstw

def get_headlines_df(df):
    headlines = df.drop(columns=['desc','site','link','img','media','2023-10-17 23:17:49.446507'], axis=1)
    return headlines

def generate_txt(df, filename):
    filename = input("Please enter file name expected: ->  ")
    # Extract the specified column as a Pandas Series & Save the column data as text in a .txt file
    column_data = df["title"]
    column_data.to_csv(filename, header=False, index=False, sep='\t')
    return print("Saved succesfully. The titles have been saved as text in {filename}'")

def get_scores(df):
    scores = []
    for i in range(len(df)):
        tokens = df["tokens"][i]
        sentiment_score = analyzer.polarity_scores(' '.join(tokens))['compound']
        scores.append(sentiment_score)
        i + 1

    df["score"] = scores

    return df

def extract_named_entities(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    words = nltk.word_tokenize(cleaned_text)
    pos_tags = nltk.pos_tag(words)
    named_entities = nltk.ne_chunk(pos_tags)
    return named_entities

#codigo a auditar #!!!!!!!!!!!!!!!!!!!!!!!
def extract_entities(text_file):
    with open(text_file, 'r') as f:
        text = f.read()
    entities = {}
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                entity = ' '.join(c[0] for c in chunk)
                entities[entity] = entities.get(entity, 0) + 1
    return entities
#------

if __name__ == "__main__":
    working_directory = "/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/"
    file_name = "news_data_Israel_1697595469.csv"
    #import csv
    df = file_to_df(working_directory, file_name)
    #transform to optimize for semantic analysis in various forms
    df['tokens'] = df['title'].apply(clean_text)
    #simplify for analysis
    headlines = get_headlines_df(df)
    #obtain sentiment score
    get_scores(headlines)
    #save results by date to csv - txt
    filename = "Israel.txt" #!!!!!!!!!!!!!!!!!!!!!!!
    generate_txt(headlines, filename)
    #obtain main entities involved & save top 10 to subject by date
    headlines["named_entities"] = headlines["title"].apply(extract_named_entities)
    #save to CSV
    output_csv = "processed news" #!!!!!!!!!!!!!!!!!!!!!!!
    headlines.to_csv(output_csv, header=False, index=False, sep='\t') 
    #generate main entities & sort them 
    entities = extract_entities(filename)
    sorted_entities = dict(sorted(entities.items(), key=lambda item: item[1], reverse=True))
    #also save to csv
    output_csv_2 = "main_entities"
    sorted_entities.to_csv(output_csv_2, header=False, index=False, sep='\t') 

    print("Sub_process complete")
