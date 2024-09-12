from google.cloud import texttospeech
import os
import fitz

doc = fitz.open('example.pdf')
text = ""
for page in doc:
    text += page.get_text()

doc.close()

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] must be set to your text-to-speech

client = texttospeech.TextToSpeechClient()

text_bock = text

synthesis_input = texttospeech.SynthesisInput(text=text_bock)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Studio-O"
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    effects_profile_id=['small-bluetooth-speaker-class-device'],
    speaking_rate=1,
    pitch=1
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

with open("output.mp3", "wb") as output:
    output.write(response.audio_content)
    print("Audio content written to file 'output.mp3'")
