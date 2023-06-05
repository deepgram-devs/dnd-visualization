from deepgram import Deepgram
import json, os

# Feel free to modify your model's parameters as you wish!
params = {
    "punctuate": True,
    "model": 'general',
    "tier": 'nova',
    "summarize": True,
    "detect_topics": True
}

#This function is what calls on the model to transcribe
def transcribe_dg(mimetype, directory, dg_key):
    dg = Deepgram(dg_key)
    audio_folder = os.listdir(directory)
    for audio_file in audio_folder:
        if audio_file.endswith(mimetype):
          with open(f"{directory}/{audio_file}", "rb") as f:
              source = {"buffer": f, "mimetype":'audio/'+mimetype}
              res = dg.transcription.sync_prerecorded(source, params)
              with open(f"deepgram_output/{audio_file[:-4]}.json", "w") as transcript:
                  json.dump(res, transcript)
    return