import requests
import json, os

ADDITIVES = 'realistic, fantasy, dungeons & dragons'
SEPARATOR = '######################################################'

'''
This function takes the full transcript from each output JSON
in `deepgram_output` and turns it into an image using Stable Diffusion
'''
def create_images(stable_key, transcript_directory):
    url = "https://stablediffusionapi.com/api/v3/text2img"

    transcript_folder = os.listdir(transcript_directory)

    for transcript_file in transcript_folder:

        with open(transcript_file, "r") as file:
            data = json.load(file)

            # This variable contains the full transcript of the audio.
            # If you wish to incorporate the summary or topics detected, parse the json as you see fit!
            transcript = data['results']['channels'][0]['alternatives'][0]['transcript']

            payload = json.dumps({
            "key": stable_key,
            "prompt": ADDITIVES + transcript,
            "negative_prompt": None,
            "width": "512",
            "height": "512",
            "samples": "1",
            "num_inference_steps": "20",
            "seed": None,
            "guidance_scale": 7.5,
            "safety_checker": "yes",
            "multi_lingual": "no",
            "panorama": "no",
            "self_attention": "no",
            "upscale": "no",
            "embeddings_model": "embeddings_model_id",
            "webhook": None,
            "track_id": None
            })

            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            print('\n' + SEPARATOR + '\n')
