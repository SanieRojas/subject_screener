
    #set up topics to monitor 
from datetime import datetime
from 
from sub_search.sub_search import setup_engine, setup_subject
from sub_process.sub_process import 

FOLDER_RAW = "C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/raw/accum/"
FOLDER_DFS = "C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/processed/dataframes/"
FOLDER_TXT = "C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/processed/text/"
FOLDER_JSON = "C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/processed/jsons/"

FOLDER_RAW_GCS = "gs://subject-screener1/raw_data/"
FOLDER_DFS_GCS = "gs://subject-screener1/dfs/"
FOLDER_TXTS_GCS = "gs://subject-screener1/txts/"
FOLDER_JSON_GCS = "gs://subject-screener1/jsons/"
BUCKET_NAME = "subject-screener1"
DATASET_ID = "compiled_data"
TABLE_ID_1 = "news_by_subject"
TABLE_ID_2 = "hourly_scores_by_subject"


logstamp = datetime.now().timestamp() 

storage_client = storage.Client()


topics =  ["Middle-East-Tensions", 
               "Rusia-China-Alliance", 
               "US-Military", 
               "Cybersecurity-threats", 
               "energy-resources", 
               "aerospace", 
               "infrastructure-vulnerabilities", 
               "financial-markets", 
               "supranational-events"]

    #call the functions every 1 hour 
for topic in topics:
    step1 = setup_engine("1h") #sub_search.sub_search_accumulate.py
    step2 = setup_subject(step1, topic, "yes") #sub_search.sub_search_accumulate.py
    print(f"Subject retrieved succesfully: {topic}")

#extract saving function and adapt to GCS 
#acumulate the data - compute engine  
#process the data 
#save the data into its different folder results 



