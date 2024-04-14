## Activate venv(Not necessary just makes a clean environment) 

    . dreamcanvas/replicate/.venv/bin/activate (From SEMN dir (Linux command))

## Setup glcoud CLI (If needed, I will have to add you to gcs)
    https://cloud.google.com/docs/authentication/provide-credentials-adc#how-to

## Set the API token and Google Cloud creds (shouldnt be necessary if using venv)
Run in terminal
    export REPLICATE_API_TOKEN=***
    export GOOGLE_APPLICATION_CREDENTIALS="dreamcanvas/replicate/dreamcanvas-***.json"
    
## Running API

    python3 (path)/dreamscapeAPI.py

## API calls from terminal
Run in terminal

    Host and Train:
    curl -X POST -F "zip_file=@(PATH TO FILE).zip" http://localhost:5000/upload_and_train

    Generate Image:
    curl -X POST -F "prompt=\"(Your prompt)\"" -F "lora_url=\"(Output from Train function)"" http://localhost:5000/generate_image

    Host Photos Only:
    curl -X POST -F "zip_file=@(PATH TO FILE).zip" http://localhost:5000/host_photos

    Train Only:
    curl -X POST -d "zip_url=\"(Output url of Host function)"" http://localhost:5000/train_model

    All urls should be outputted to terminal

