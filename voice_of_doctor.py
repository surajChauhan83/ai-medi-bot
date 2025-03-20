import os
import platform
import subprocess
from gtts import gTTS
from pydub import AudioSegment

def text_to_speech_with_gtts(input_text, output_filepath):
    if os.path.exists(output_filepath):
        os.remove(output_filepath)  # Delete the old file if it exists

    # Generate MP3 file
    audioObj = gTTS(
        text=input_text,
        lang="en",
        slow=False
    )
    audioObj.save(output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # Convert MP3 to WAV
            wav_filepath = output_filepath.replace(".mp3", ".wav")
            sound = AudioSegment.from_mp3(output_filepath)
            sound.export(wav_filepath, format="wav")

            # Play the WAV file in PowerShell
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync()'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"An error occurred: {e}")
#step1: Setup Text to Speech-TTS-model with gTTS

# import os
# from gtts import gTTS

# def text_to_speech_with_gtts(input_text, output_filepath):
#     audioObj = gTTS(
#         text=input_text,
#         lang="en",
#         slow=False
#     )
#     # Save the generated speech to the specified file
#     audioObj.save(output_filepath)
#     print(f"Audio saved to {output_filepath}")

# input_text = "Hi, I am Suraj"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")


#step1: Setup Text to Speech-TTS-model with  ElevenLab
# import elevenlabs
# from elevenlabs.client import ElevenLabs
# ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# def text_to_speech_with_elevenlabs(input_text,output_filepath):
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.generate(
#         text=input_text,
#         voice="Aria",
#         output_format="mp3_22050_32",
#         model="eleven_turbo_v2"
#     )
#     elevenlabs.save(audio,output_filepath)

# text_to_speech_with_elevenlabs(input_text,output_filepath="elevenlabs_testing.mp3")


# def text_to_speech_with_gtts(input_text, output_filepath):
#     if os.path.exists(output_filepath):
#         os.remove(output_filepath)  # Delete the old file if it exists

#     audioObj = gTTS(
#         text=input_text,
#         lang="en",
#         slow=False
#     )
#     audioObj.save(output_filepath)

#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync()'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])
#         else:
#             raise OSError("Unsupported OS")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# input_text = "Hi, I am Suraj Chauhan, new version testing"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")
