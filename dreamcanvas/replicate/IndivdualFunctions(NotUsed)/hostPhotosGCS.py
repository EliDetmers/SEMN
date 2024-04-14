from google.cloud import storage
from datetime import timedelta
storage_client = storage.Client.from_service_account_json('dreamcanvas/SEMN/dreamcanvas-***.json')

def upload_to_gcs(bucket_name, file_path, destination_blob_name):
    # Initialize the GCS client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Upload the file to GCS
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(file_path)

    print(f'File {file_path} uploaded to {destination_blob_name} in bucket {bucket_name}')

    url = blob.generate_signed_url(
    version="v4",
    expiration=timedelta(days=1),
    method="GET"
    )
    print(f'Signed URL for the uploaded file: {url}')



# Example usage:
bucket_name = 'gcs-dreamscape-uploads'
file_path = 'dreamcanvas/replicate/Pappa.zip'
destination_blob_name = 'Pappa.zip'

upload_to_gcs(bucket_name, file_path, destination_blob_name)

