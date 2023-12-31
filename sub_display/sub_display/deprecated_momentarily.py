"""code removed momentarily due to dependency hell"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

import nltk
from nltk.tokenize import word_tokenize
nltk.download(['stopwords', 'vader_lexicon', 'punkt'], quiet=True) 
stopwords = nltk.corpus.stopwords.words("english")

folder_pointer = "C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/processed/"
folder_txt = f'{folder_pointer}text/'
#folder_json =  f'{folder_pointer}jsons/'
#folder_dfs =   f'{folder_pointer}dataframes/'
file_pointer = "predictions_2024_v2.txt"
subject = "test_display"


newsfeed = pd.read_csv(f'{folder_txt}{file_pointer}')
text = " ".join(line.split()[1] for line in newsfeed["title"])

wordcloud = WordCloud(width=480, height=480, stopwords = stopwords, background_color= "white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

plt.title(f"Wordcloud- {subject}")

# Save the visualization as an image
plt.savefig("wordcloud.png", dpi=300, format="png")

##wordcloud.to_file("wordcloud.png")

#wordcloud = create_wordcloud(text)
#save_wordcloud(wordcloud, "wordcloud.png")

