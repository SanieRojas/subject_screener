"""display a wordcloud of content"""
##from wordcloud import WordCloud
#import matplotlib.pyplot as plt
import pandas as pd
from pywordcloud import create_wordcloud, save_wordcloud

#import nltk
#from nltk.tokenize import word_tokenize
#nltk.download(['stopwords', 'vader_lexicon', 'punkt'], quiet=True) 
#stopwords = nltk.corpus.stopwords.words("english")

newsfeed = pd.read_csv("news_data_palestine_1697589162.csv")
text = " ".join(line.split()[1] for line in newsfeed["title"])
##wordcloud = WordCloud(width=480, height=480, stopwords = stopwords, background_color= "white").generate(text)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
#plt.margins(x=0, y=0)
#plt.show()

#plt.title("Scatter Plot Example")

# Save the visualization as an image
#plt.savefig("wordcloud.png", dpi=300, format="png")

##wordcloud.to_file("wordcloud.png")


wordcloud = create_wordcloud(text)
save_wordcloud(wordcloud, "wordcloud.png")

newsfeed.plot(x='Month', y='Sales', kind='bar')

