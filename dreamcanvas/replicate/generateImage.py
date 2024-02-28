import replicate

lora_url = "https://replicate.delivery/pbxt/FP9WZOt1yDL1KxbVB9pkaPeUAnl1dmR4C6DTUGvIkk24QhNJA/tmpfxfyd66bPappazip.safetensors"

output_url = replicate.run(
    "replicate/lora:97ec1b97e5e6a6476e45ba7211d368509bbf39c30a927e39637f3cb98b36ac91",
    input={
        "prompt": "a painting of <1> as a king",
        "lora_urls": lora_url,
    },
)
print(output_url)