## Compile all CSVs 
import os
from google.cloud import storage
from datetime import datetime
import pandas as pd 
import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/credentials/subject-screener-402918-c2016ea141c2.json"

folder_pointer = 'C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/raw/accum/'
folder_destiny = 'C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/raw/accum'
dataframes = []
topics = ["Middle-East-Tensions", "Rusia-China-Alliance", "US-Military", "Cybersecurity-threats", "Energy-resources", "aerospace", "infrastructure-vulnerabilities", "financial-markets", "supranational-events" ]

def compile_a_folder(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder, filename)
            df = pd.read_csv(file_path)
            dataframes.append(df)

    compiled_data = pd.concat(dataframes, ignore_index=True)
    return compiled_data.to_csv(f'{folder_destiny}compiled_data_accum.csv', index=False)

def compile_a_gcs_folder(folder):
    
    
    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder, filename)
            df = pd.read_csv(file_path)
            dataframes.append(df)

    compiled_data = pd.concat(dataframes, ignore_index=True)
    return compiled_data.to_csv(f'{folder_destiny}compiled_data_accum.csv', index=False)



if __name__ == "__main__":

    compile_a_folder(folder_pointer)


#generate storage client 
log2 = datetime.now().timestamp() 
bucket_name = "subject-screener1"
storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(f"raw_data/compiled_data_{log2}.txt")
blob.upload_from_filename(f"{folder_destiny}compiled_data_accum.csv")
