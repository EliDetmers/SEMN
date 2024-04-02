import replicate
output = replicate.run(
    "cloneofsimo/lora-training:b2a308762e36ac48d16bfadc03a65493fe6e799f429f7941639a6acec5b276cc",
    input={
        "task": "face",
        "resolution": 512,
        "instance_data": "https://dreambooth-api-experimental.replicate.com/v1/upload/Pappa.zip"
    }
)
print(output)