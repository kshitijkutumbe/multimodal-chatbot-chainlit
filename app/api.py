# app/api.py
from openai import OpenAI
from config import Config
from logger import setup_logger

logger = setup_logger(__name__)

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def append_messages(image_url=None, query=None, audio_transcript=None):
    try:
        message_list = []

        if image_url:
            message_list.append({"type": "image_url", "image_url": {"url": image_url}})

        if query and not audio_transcript:
            message_list.append({"type": "text", "text": query})

        if audio_transcript:
            message_list.append({"type": "text", "text": query + "\n" + audio_transcript})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": message_list}],
            max_tokens=1024,
        )
        return response.choices[0]
    except Exception as e:
        logger.error(f"Error in append_messages: {e}")
        raise

def audio_process(audio_path):
    try:
        audio_file = open(audio_path, "rb")
        transcription = client.audio.transcriptions.create(
            model="whisper-1", file=audio_file
        )
        return transcription.text
    except Exception as e:
        logger.error(f"Error processing audio: {e}")
        raise
