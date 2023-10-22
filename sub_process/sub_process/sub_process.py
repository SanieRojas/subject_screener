"""Analyzing text retrieved per subject"""

folder_pointer = 'C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/raw/'
folder_destiny = 'C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/processed/'
subject = "subject_initializer"

#importing libraries
import re
import json
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import pos_tag, ne_chunk

nltk.download(['stopwords', 'vader_lexicon', 'punkt'], quiet=True) 
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

def get_subject(file):
    """ getting subject """
    subject = file.str.slice(9, len(user_file)-6)
    return subject

def file_to_df(user_file):
    """ Process the file into a pandas dataframe."""
    user_file = input("Please enter file name to be analyzed: ->  ")
    global subject
    subject = user_file[9:-6]
    file_pointer = f"{folder_pointer}{user_file}"
    df = pd.read_csv(file_pointer)
    return df

def clean_text(text):
    """ Clean text."""
    my_stopwords = nltk.corpus.stopwords.words("english")
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    words = nltk.word_tokenize(cleaned_text)
    words_nstw = [word for word in words if word not in my_stopwords]
    return words_nstw

def get_headlines_df(df):
    """ Get headlines."""
    headlines = df.drop(columns=['desc','site','link','img','media','log_date'], axis=1)
    return headlines

def generate_txt(df):
    """ Generates .txt file for furhter analysis."""
    filename = input("Please enter file name expected for the TXT file without the extension .txt: ->  ")
    filename = filename + ".txt"
    file_pointer = f"{folder_destiny}{filename}"
    # Extract the specified column as a Pandas Series & Save the column data as text in a .txt file
    column_data = df["title"]
    column_data.to_csv(file_pointer, header=False, index=False, sep='\t')
    return print(f"Saved succesfully. The titles have been saved as text in {filename}'")

def get_scores(df):
    """ Get scores."""
    scores = []
    analyzer = SentimentIntensityAnalyzer()
    for i in range(len(df)):
        tokens = df["tokens"][i]
        sentiment_score = analyzer.polarity_scores(' '.join(tokens))['compound']
        scores.append(sentiment_score)
    df["score"] = scores
    return df

def extract_named_entities(text):
    """ Get entities."""
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    words = nltk.word_tokenize(cleaned_text)
    pos_tags = nltk.pos_tag(words)
    named_entities = nltk.ne_chunk(pos_tags)
    return named_entities

#codigo a auditar #!!!!!!!!!!!!!!!!!!!!!!!
def extract_entities(text_file):
    """ extract main entities."""
    with open(text_file, 'r',  encoding='utf-8') as f:
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

    user_file = "hi"

    #import file
    dfn = file_to_df(user_file)

    #transform to optimize for semantic analysis in various forms
    dfn['tokens'] = dfn['title'].apply(clean_text)
    #simplify for analysis
    headlines = get_headlines_df(dfn)
    #obtain sentiment score
    get_scores(headlines)
    #save results by date to csv - txt
    generate_txt(headlines)
    #obtain main entities involved & save top 10 to subject by date
    headlines["named_entities"] = headlines["title"].apply(extract_named_entities)
    #save to CSV
    output_csv = f"{folder_destiny}/dataframes/{subject}.csv"
    file_csv= headlines.to_csv(output_csv, header=False, index=False, sep='\t')
    #generate main entities & sort them
    entities = extract_entities(output_csv)
    sorted_entities = dict(sorted(entities.items(), key=lambda item: item[1], reverse=True))
    #also save to json
    with open(f"{folder_destiny}/jsons/sorted_entities_{subject}.json", "w") as file:
        json.dump(sorted_entities, file)
    print("Sub_process complete")
