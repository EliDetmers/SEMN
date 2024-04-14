from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from google.cloud import storage
from datetime import timedelta
import os
import replicate
import requests

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
API_KEY = "r8_***"
storage_client = storage.Client.from_service_account_json('replicate/dreamcanvas-***.json')

# def host_photos(zip_file):
#     zip_filename = secure_filename(zip_file.filename)
#     #zip_path = os.path.join(zip_filename)
#     #zip_file.save(zip_path)

#     upload_response = requests.post(
#         "https://dreambooth-api-experimental.replicate.com/v1/upload/" + zip_filename,
#         headers={"Authorization": "Token " + API_KEY},
#     ).json()

#     with open(zip_filename, "rb") as f:
#         requests.put(upload_response["upload_url"], data=f)

#     return upload_response["serving_url"]

def host_photos(file_path):
    bucket_name = "gcs-dreamscape-uploads"
    # Initialize the GCS client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)
    print('bucket')
    # Extract filename from file_path
    destination_blob_name = secure_filename(file_path.filename)
    print('extract')
    # Upload the file to GCS
    blob = bucket.blob(destination_blob_name)
    file_path.seek(0)
    blob.upload_from_file(file_path)

    print(f'File {file_path} uploaded to {destination_blob_name} in bucket {bucket_name}')

    url = blob.generate_signed_url(
        version="v4",
        expiration=timedelta(days=1),
        method="GET"
    )
    print(f'Signed URL for the uploaded file: {url}')

    return url

# Example usage:
# bucket_name = 'gcs-dreamscape-uploads'
# file_path = 'dreamcanvas/replicate/Pappa.zip'
# destination_blob_name = 'Pappa.zip'


def train_model(zip_url):
    output = replicate.run(
        "cloneofsimo/lora-training:b2a308762e36ac48d16bfadc03a65493fe6e799f429f7941639a6acec5b276cc",
        input={
            "task": "face",
            "resolution": 512,
            "instance_data": zip_url
        }
    )
    
    return output

@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data['prompt']
    lora_url = data['lora_url']
    
    output_url = replicate.run(
        "replicate/lora:97ec1b97e5e6a6476e45ba7211d368509bbf39c30a927e39637f3cb98b36ac91",
        input={
            "prompt": prompt,
            "lora_url": lora_url
        }
    )
    
    return jsonify({'output_url': output_url})

@app.route('/upload_and_train', methods=['POST'])
def upload_and_train():
    zip_file = request.files.get('zip_file')
    zip_url = host_photos(zip_file)
    print("Zip_url: " + zip_url)
    lora_url = train_model(zip_url)
    print("lora_url: " + lora_url)
    
    return jsonify({'lora_url': lora_url})

@app.route('/host_photos', methods=['POST'])
def api_host_photos():
    zip_file = request.form.get('file_path')
    url = host_photos(zip_file)
    return jsonify({'signed_url': url})

@app.route('/train_model', methods=['POST'])
def api_train_model():
    zip_url = request.form['zip_url']
    lora_url = train_model(zip_url)
    return jsonify({'lora_url': lora_url})

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(debug=True)
 
