# Project Report:Automating ETL Pipeline for Sports Data Analytics

# #Overview
This project automates the ETL pipeline for fetching cricket player rankings data, storing it in Google Cloud Storage (GCS), triggering a Dataflow job to load the data into BigQuery, and visualizing it using Looker Studio. The entire process is automated using Apache Airflow for seamless execution.
Architecture Diagram
 
Data Retrieval:
Data is fetched from the Cricbuzz API using Python, specifically the rankings for Test cricket batsmen.
•	API Request: A GET request is made to the Cricbuzz API, specifying Test cricket rankings.
•	Data Extraction: The player rank, name, and country are extracted from the API response and stored in CSV format.

Storing Data in GCS:
After data extraction, it is saved in a CSV file and uploaded to Google Cloud Storage (GCS) for further processing.
•	CSV Writing: The data is written to a CSV file (batsmen_rankings2.csv).
•	GCS Upload: The file is uploaded to a designated GCS bucket (cricdatabucket2).

Cloud Function Trigger:
A Cloud Function is set to trigger whenever a new CSV file is uploaded to GCS, which then triggers a Dataflow job to load the data into BigQuery.
•	Cloud Function: Detects new file uploads in the GCS bucket and passes parameters to the Dataflow job.

Dataflow Job:
The Dataflow job processes the uploaded CSV file, transforming the data and loading it into BigQuery.
•	Schema Definition: BigQuery schema is defined in bq2.json for player ID, name, and country.
•	Data Transformation: A UDF (udf2.js) processes each CSV row to convert it into structured JSON.
•	Data Loading: The transformed data is loaded into BigQuery for analysis.

Looker Studio Visualization:
Once the data is in BigQuery, Looker Studio is used to create interactive dashboards.
•	Looker Configuration: Looker Studio is connected to BigQuery to visualize the cricket player rankings data.






Looker Visualization
 
Apache Airflow Automation
The ETL pipeline is automated using Apache Airflow:
1.	Default Arguments: Configures task owner, start date, retry policies, and notification settings.
2.	DAG Definition: The DAG (fetch_batsmenranking_stats) runs daily (@daily), ensuring automated execution without manual intervention.
3.	Task (BashOperator): A task runs the Python script (ExtractPushToGCS2.py) to fetch and upload data.
4.	Execution Flow: The DAG triggers the task daily, with retries in case of failure, ensuring continuous execution.
   
Conclusion:
The ETL pipeline is fully automated using Apache Airflow, ensuring timely data retrieval, processing, and visualization. Data is fetched from the Cricbuzz API, processed, stored in GCS, and loaded into BigQuery for analysis. Looker Studio provides insights into cricket player rankings. The daily schedule and error handling mechanisms ensure the pipeline runs smoothly with minimal human intervention.
![image](https://github.com/user-attachments/assets/8c4f8caf-f0d3-431a-a7aa-cf9eecdc2ce3)
