import logging
import speech_recognition as sr 
import os
from groq import Groq
from pydub import AudioSegment
from io import BytesIO

# Fix Logging Format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded file.
    timeout (int): Max time to wait for speech start (seconds).
    phrase_time_limit (int): Max duration of speech recording (seconds).
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")

            # Record the audio 
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            # Convert the recorded audio to MP3
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def trascript_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    audio_file=open(audio_filepath,"rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )
    return transcription.text

# Run the function
# audio_filepath = "patient_voice_test.mp3"
# record_audio(file_path=audio_filepath)


#step2: setup speech to text-STT-model for transcription

# import os
# from groq import Groq

# GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# client = Groq(api_key=GROQ_API_KEY)
# stt_model="whisper-large-v3"

# audio_file=open(audio_filepath,"rb")
# transcription=client.audio.transcriptions.create(
#     model=stt_model,
#     file=audio_file,
#     language="en"
# )

# print(transcription.text)
# def trascript_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
#     client = Groq(api_key=GROQ_API_KEY)
#     audio_file=open(audio_filepath,"rb")
#     transcription=client.audio.transcriptions.create(
#         model=stt_model,
#         file=audio_file,
#         language="en"
#     )
#     return transcription.text

