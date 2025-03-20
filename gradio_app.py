#voice bot UI with gradio
import os
import base64
import tempfile
import gradio as gr
from brain_of_doctor import encode_images, analyze_img_with_query
from voice_of_patient import record_audio, trascript_with_groq
from voice_of_doctor import text_to_speech_with_gtts

systme_prompt = """You have to act as a doctor, I know you are not, but this is for learning purposes.
With what I see, I think you have .... 
Do you find anything wrong with it medically?
If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in your response.
Your response should be in one long paragraph. Also, always answer as if you are speaking to a real person.
Do not say 'In the image, I see' but say 'With what I see, I think you have ....'
Do not respond as an AI model in markdown. Your answer should mimic an actual doctor, not an AI bot.
Keep your answer concise (max 2 sentences). No preamble, start your answer right away, please."""

def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = trascript_with_groq(stt_model="whisper-large-v3",audio_filepath=audio_filepath, GROQ_API_KEY = os.environ.get("GROQ_API_KEY"))

    #handle the image input 
    if image_filepath:
        doctor_response = analyze_img_with_query(query=systme_prompt+speech_to_text_output,model="llama-3.2-90b-vision-preview", encode_image=encode_images(image_filepath), GROQ_API_KEY = os.environ.get("GROQ_API_KEY"))
    else:
        doctor_response = "No image provide for me to analysis"

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_audio:
        text_to_speech_with_gtts(doctor_response, temp_audio.name)
        voice_of_doctor = temp_audio.read()

    # voice_of_doctor = text_to_speech_with_gtts(doctor_response, "final.mp3")

    return speech_to_text_output, doctor_response, voice_of_doctor
#create the interface

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="🎤 Speak Your Symptoms"),
        gr.Image(type="filepath", label="🖼 Upload Medical Image")
    ],
    outputs=[
        gr.Textbox(label="📝 Patient's Voice Transcription", interactive=False),
        gr.Textbox(label="💡 Doctor's AI Response", interactive=False),
        gr.Audio(label="🔊 Doctor's Voice Reply", interactive=False)
    ],
    title="AI Doctor: Voice & Vision Assistant",
    description="👩‍⚕️ A smart AI-powered doctor that listens to your symptoms, analyzes images, and responds like a real doctor!"
)

iface.launch(debug=True)

