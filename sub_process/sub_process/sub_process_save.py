## Compile all CSVs 
import os
from google.cloud import storage, bigquery
from datetime import datetime
import pandas as pd 
import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/credentials/subject-screener-402918-c2016ea141c2.json"

folder_pointer = 'C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/raw/accum/'
folder_destiny = 'C:/Users/sanie.s.rojas.lobo/Desktop/ITBA Bucket/subject_screener/file_store_search/processed/dataframes/'
dataframes = []
topics = ["Middle-East-Tensions", "Rusia-China-Alliance", "US-Military", "Cybersecurity-threats", "Energy-resources", "aerospace", "infrastructure-vulnerabilities", "financial-markets", "supranational-events" ]


#generate storage client 
log2 = datetime.now().timestamp() 
bucket_name = "subject-screener1"
storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(f"raw_data/compiled_data_{log2}.csv")
blob.upload_from_filename(f"{folder_destiny}data_acc.csv")

project_id = "subject-screener"
dataset_id = "compiled_data"
table_id = "news_by_subject"

client = bigquery.Client()
job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV)
uri = f"gs://subject-screener1/raw_data/compile_data_{log2}.csv"

#title,date,datetime,subject,tokens,score


schema = [
    bigquery.SchemaField("title", "STRING"),
    bigquery.SchemaField("date", "STRING"),
    bigquery.SchemaField("datetime", "DATETIME"),
    bigquery.SchemaField("subject", "STRING"),
    bigquery.SchemaField("tokens", "STRING"),
    bigquery.SchemaField("score", "FLOAT"),
    #bigquery.SchemaField("site", "FLOAT"),
    
    # Define the schema for all columns in your CSV
]


job_config = bigquery.LoadJobConfig(
    schema=schema,
    skip_leading_rows=1,  # Skip the CSV header row
    source_format=bigquery.SourceFormat.CSV,
)

# Create the BigQuery table
table_ref = client.dataset(dataset_id).table(table_id)
load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)

# Wait for the job to complete
load_job.result()

