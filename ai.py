import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def preguntar(mensaje):
    respuesta = client.responses.create(
        model="gpt-5-mini",
        input=mensaje
    )

    return respuesta.output_text