# dnd-visualization

This repository contains an AI speech-to-image pipeline. It was constructed by piping the output of Deepgram's speech-to-text API into Stable Diffusion's text-to image API. Below, you'll find descriptions of each of the files and folders within this repository. However, if you'd like to see a video-tutorial and demo of this code, check out the following video: 

Link to video ▶️🎥 - [Unleashing AI Magic: Visualizing Dungeons & Dragons with Stable Diffusion and Deepgram](https://youtu.be/MR6DTMGbGX0) 

<img width="949" alt="Screen Shot 2023-06-05 at 1 34 31 PM" src="https://github.com/deepgram-devs/dnd-visualization/assets/57232352/4597749f-57d0-4c27-a782-12e96cd9c48d">

Also, if you'd like to sign up for Deepgram to receive up to 45000 minutes of transcription for free (without even having to put down a credit card), check out [this link](https://dpgr.am/youtube)

**The files**

`main.py` - You can run this file by entering `python3 main.py` into the command line. It will take a series of videos that you specify, transcribe them, and use those transcriptions to create images. As of right now, the code works best with short snippets of people describing their own *Dungeons & Dragons* characters or the setting(s) of the quest.

`deepgram_inference.py` - Given an audio, this file will us Deepgram's AI models to output a JSON that contains a transcription of the audio, a summary of the audio, and a list of the audio's main topics.

`stable_diffusion.py` - The way the starter code is written, this file will read the output transcription of the Deepgram models and use that text to create images. Check out the `ADDITIVES` constant within the file to further modify the prompt that the AI will use to create images.

`youtube_download.py` - Given a list of video URLs from YouTube, this file will extract the audios of those videos as mp3 files.
