def extract_and_load_to_df():
    # Extrae los datos de la API
    response = requests.get('http://api.example.com/data')
    data = response.json()

    # Carga los datos en un DataFrame de pandas
    df = pd.DataFrame(data)

    # Guarda el DataFrame en el XComs para que esté disponible para otras tareas
    return df.to_json()

def save_to_gcs(**context):
    # Carga el DataFrame desde XComs
    df_json = context['task_instance'].xcom_pull(task_ids='extract_and_load_to_df')
    df = pd.read_json(df_json)

    # Guarda el DataFrame en un archivo parquet
    df.to_parquet('data.parquet')

    # Sube el archivo parquet a Google Cloud Storage
    hook = GoogleCloudStorageHook(google_cloud_storage_conn_id='my_gcs_connection')
    hook.upload(bucket='my_bucket', object='data.parquet', filename='/path/to/data.parquet')

def load_to_bq():
    # Crea la tabla en BigQuery a partir del archivo parquet en Google Cloud Storage
    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.PARQUET)
    uri = "gs://my_bucket/data.parquet"
    dataset_ref = client.dataset('my_dataset')
    table_ref = dataset_ref.table('my_table')
    
    load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
    load_job.result()
    

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1)
}

dag = DAG('api_to_bq', 
          description='Extract data from API, load into pandas, save to GCS, and load to BQ',
          schedule_interval='0 12 * * *',
          default_args=default_args,
          catchup=False)

task1 = PythonOperator(task_id='extract_and_load_to_df', 
                       python_callable=extract_and_load_to_df, 
                       provide_context=True,
                       dag=dag)

task2 = PythonOperator(task_id='save_to_gcs', 
                       python_callable=save_to_gcs, 
                       provide_context=True,
                       dag=dag)

task3 = PythonOperator(task_id='load_to_bq', 
                       python_callable=load_to_bq, 
                       dag=dag)

task1 >> task2 >> task3