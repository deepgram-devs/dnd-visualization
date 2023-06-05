# dnd-visualization

This repository contains an AI speech-to-image pipeline. It was constructed by piping the output of Deepgram's speech-to-text API into Stable Diffusion's text-to image API. Below, you'll find descriptions of each of the files and folders within this repository. However, if you'd like to see a video-tutorial and demo of this code, check out the following video: 

Link to video ▶️🎥 - [Unleashing AI Magic: Visualizing Dungeons & Dragons with Stable Diffusion and Deepgram](https://youtu.be/MR6DTMGbGX0) 

<img width="949" alt="Screen Shot 2023-06-05 at 1 34 31 PM" src="https://github.com/deepgram-devs/dnd-visualization/assets/57232352/4597749f-57d0-4c27-a782-12e96cd9c48d">

Also, if you'd like to sign up for Deepgram to receive up to 45000 minutes of transcription for free (without even having to put down a credit card), check out [this link](https://dpgr.am/youtube)

# The files

`main.py` - You can run this file by entering `python3 main.py` into the command line. It will take a series of videos that you specify, transcribe them, and use those transcriptions to create images. As of right now, the code works best with short snippets of people describing their own *Dungeons & Dragons* characters or the setting(s) of the quest.

`deepgram_inference.py` - Given an audio, this file will us Deepgram's AI models to output a JSON that contains a transcription of the audio, a summary of the audio, and a list of the audio's main topics.

`stable_diffusion.py` - The way the starter code is written, this file will read the output transcription of the Deepgram models and use that text to create images. Check out the `ADDITIVES` constant within the file to further modify the prompt that the AI will use to create images.

`youtube_download.py` - Given a list of video URLs from YouTube, this file will extract the audios of those videos as mp3 files.

# Demo
To see a demo, check out the first 45 seconds of [this video](https://youtu.be/MR6DTMGbGX0). However, for convenience, Here is another set of result images:

[This](https://youtu.be/P8pLvV3FjPc?t=1155) is the audio (19:15 - 20:14). Note that an mp3 version of this audio is available in the `audios` folder of the starter code: `laudna_dnd.mp3`.

After running that audio through the code in this repository, the following images resulted:
<img width="478" alt="Screen Shot 2023-06-05 at 1 52 55 PM" src="https://github.com/deepgram-devs/dnd-visualization/assets/57232352/b9a7fc9c-6234-44fa-bbda-388409eac2d3">
<img width="484" alt="Screen Shot 2023-06-05 at 1 53 05 PM" src="https://github.com/deepgram-devs/dnd-visualization/assets/57232352/74731106-462a-4cf0-8e50-4dd80b92e503">
<img width="465" alt="Screen Shot 2023-06-05 at 1 53 14 PM" src="https://github.com/deepgram-devs/dnd-visualization/assets/57232352/0fc358f7-4960-4c7a-ad5a-d1a5ca467b31">

(Note: In actuality, these images were produced by Stable Horde's Deliberate rather than Stable Diffusion. As mentioned in the video tutorial, you can swap out the text-to-image generator as you see fit! 😊)

For comparison, here is the canonical image of the character, named Laudna, from the [Critical Role wiki](https://criticalrole.fandom.com/wiki/Laudna)

<img width="470" alt="Screen Shot 2023-06-05 at 1 53 37 PM" src="https://github.com/deepgram-devs/dnd-visualization/assets/57232352/aa0164ea-2a9c-448b-b483-88d32a7e7ca9">

