import os
import requests

zip_path = "/Pappa.zip"
zip_filename = zip_path.split("/")[-1]

# Upload inputs to cloud storage.
# You can skip this step if your zip file is already on the internet and accessible over HTTP
upload_response = requests.post(
    "https://dreambooth-api-experimental.replicate.com/v1/upload/" + zip_filename,
    headers={"Authorization": "Token " + os.environ["REPLICATE_API_TOKEN"]},
).json()

with open(zip_path, "rb") as f:
    requests.put(upload_response["upload_url"], data=f)
zip_url = upload_response["serving_url"]