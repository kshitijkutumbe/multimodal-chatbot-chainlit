from openai import OpenAI
import base64
import chainlit as cl
import os
from api import append_messages,audio_process
from utils import image2base64

@cl.on_chat_start
async def start():
    text_content = "Author: Kshitij Kutumbe"
    elements = [
        cl.Text(name="", content=text_content, display="inline")
    ]

    await cl.Message(
        content="",
        elements=elements,
    ).send()

@cl.on_message
async def chat(msg: cl.Message):

    images = [file for file in msg.elements if "image" in file.mime]
    audios = [file for file in msg.elements if "audio" in file.mime]

    if len(images) > 0:
        base64_image = image2base64(images[0].path)
        image_url = f"data:image/png;base64,{base64_image}"

    elif len(audios) > 0:
        text = audio_process(audios[0].path)

    response_msg = cl.Message(content="")

    if len(images) == 0 and len(audios) == 0:
        response = append_messages(query=msg.content)

    elif len(audios) == 0:
        response = append_messages(image_url=image_url, query=msg.content)

    else:
        response = append_messages(query=msg.content, audio_transcript=text)

    response_msg.content = response.message.content

    await response_msg.send()