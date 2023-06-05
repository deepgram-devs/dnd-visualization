from youtube_download import download_audios
from deepgram_inference import transcribe_dg
from stable_diffusion import create_images

# A list of URLs (type: string)
vids = ['URL to desired video here']

'''
The code in `deepgram_inference` will transcribe all
files in `directory` that end with `mimetype`.

(Starter-code default: Transcribe all mp3 files in ./audios)
'''
mimetype = 'mp3'
audio_directory = './audios'
transcript_directory = './deepgram_output'


# API Keys go here. Or, you can set them up as 
# environment variables.
deepgram_key = '🔑🔑🔑 Your key here 🔑🔑🔑'
stable_key = '🔑🔑🔑 Your key here 🔑🔑🔑'


'''
This function takes the videos in `vids`, extracts their audio as .mp3 files,
and then passes those mp3 files through a Speech-to-Image pipeline built
with Deepgram and Stable Diffusion.

To see the images, check out the "output" entry in Stable Diffusion's 
Responses, which will be printed to the console. 

Check out the video tutorial for this code here: https://youtu.be/MR6DTMGbGX0
'''
def main():
    download_audios(vids, audio_directory)
    transcribe_dg(mimetype, audio_directory, deepgram_key)
    create_images(stable_key, transcript_directory)