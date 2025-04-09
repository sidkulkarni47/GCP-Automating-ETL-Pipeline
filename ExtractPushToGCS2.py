import requests
import csv
from google.cloud import storage

# API request details
url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"
querystring = {"formatType":"test"}

headers = {
    "x-rapidapi-key": "e31d3f70f4mshc93c76f8615f85cp1e57e6jsn4053a3d79d1b",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

# Send GET request to API
response = requests.get(url, headers=headers, params=querystring)
print(response.json())

# Check for successful API response
if response.status_code == 200:
    data = response.json().get('rank', [])  # Extract 'rank' data from response
    csv_filename = 'batsmen_rankings2.csv'

    if data:
        field_names = ['rank', 'name', 'country']  # Define field names

        # Open CSV for writing data (excluding header)
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            # Do not write header
            # writer.writeheader()

            # Write data rows
            for entry in data:
                writer.writerow({
                    'rank': int(entry.get('rank', 0)),  # Convert rank to int
                    'name': str(entry.get('name', '')).strip(),  # Strip spaces from name
                    'country': str(entry.get('country', '')).strip()  # Strip spaces from country
                })

        print(f"Data fetched successfully and written to '{csv_filename}'")

        # Upload the CSV file to Google Cloud Storage (GCS)
        bucket_name = 'cricdatabucket2'  # Your target GCS bucket
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}'  # The GCS path where the file will be stored

        # Create a blob object and upload the file
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        print(f"File '{csv_filename}' uploaded to GCS bucket '{bucket_name}' as '{destination_blob_name}'")
    else:
        print("No data available from the API.")
else:
    print("Failed to fetch data:", response.status_code)
