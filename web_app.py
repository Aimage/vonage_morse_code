from flask import Flask, request
from config import SOUND_BASE_PATH
from vonage_api import make_vonage_call, create_vonage_api_client
from morse.encoder import message_to_morse_sound

app = Flask('__name__')


@app.route("/hello")
def hello():
    return "hello"


@app.route("/tomorseaudio")
def tomorseaudio():
    text = request.args.get("text", "")
    if text:
        message_to_morse_sound(text, SOUND_BASE_PATH, "static/output.ogg")
    return f"'{text}' translated to morse code", 200


@app.route("/sendmorse")
def morse_stream():
    base_url = request.base_url
    stream_url = f"{base_url}/static/output.ogg"
    make_vonage_call(client, stream_url)
    return "audio morse code sent"


if __name__ == '__main__':
    app.run()
