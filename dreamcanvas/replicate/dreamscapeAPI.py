from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import replicate
import requests

app = Flask(__name__)

UPLOAD_FOLDER = 'replicate'
API_KEY = os.environ["REPLICATE_API_TOKEN"]

def host_photos(zip_file):
    zip_filename = secure_filename(zip_file.filename)
    #zip_path = os.path.join(zip_filename)
    #zip_file.save(zip_path)

    upload_response = requests.post(
        "https://dreambooth-api-experimental.replicate.com/v1/upload/" + zip_filename,
        headers={"Authorization": "Token " + API_KEY},
    ).json()

    with open(zip_filename, "rb") as f:
        requests.put(upload_response["upload_url"], data=f)

    return upload_response["serving_url"]

def train_model(zip_url):
    output = replicate.run(
        "cloneofsimo/lora-training:b2a308762e36ac48d16bfadc03a65493fe6e799f429f7941639a6acec5b276cc",
        input={
            "task": "face",
            "resolution": 512,
            "instance_data": zip_url
        }
    )

    return output["lora_url"]

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.form['prompt']
    lora_url = request.form['lora_url']

    output_url = replicate.run(
        "replicate/lora:97ec1b97e5e6a6476e45ba7211d368509bbf39c30a927e39637f3cb98b36ac91",
        input={
            "prompt": prompt,
            "lora_url": lora_url
        }
    )
    print("Output Url: " + output_url)
    
    return jsonify({'output_url': output_url})

@app.route('/upload_and_train', methods=['POST'])
def upload_and_train():
    zip_file = request.files['zip_file']
    zip_url = host_photos(zip_file)
    print("Zip_url: " + zip_url)
    lora_url = train_model(zip_url)
    print("lora_url: " + lora_url)
    
    return jsonify({'lora_url': lora_url})

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(debug=True)
