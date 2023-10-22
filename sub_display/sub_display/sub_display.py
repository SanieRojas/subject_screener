"""display a wordcloud of content"""

import pandas as pd
import matplotlib.pyplot as plt 

folder_pointer = "C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/processed/"
folder_txt = f'{folder_pointer}text/'
folder_json =  f'{folder_pointer}jsons/'
folder_dfs =   f'{folder_pointer}dataframes/'
file_pointer = "data_acc.csv"
subject = "data_acc_1"

folder_destiny = "C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/images/"

newsfeed = pd.read_csv(f'{folder_dfs}{file_pointer}')
metadata= newsfeed.drop(columns=['title', 'tokens'], axis=1)

metadata["datetime"] = pd.to_datetime(metadata["datetime"])
metadata["score"] = metadata["score"].astype(float)

average_score= metadata['score'].mean()

daily_indexed = metadata.set_index('datetime')
mean_by_day = daily_indexed["score"].resample('D').mean()

print(average_score, mean_by_day)

daily_score = mean_by_day.plot()
plt.savefig(f'{folder_destiny}line_plot_{subject}.png', dpi=300, bbox_inches='tight')

