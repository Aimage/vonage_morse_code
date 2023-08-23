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
    to = request.args.get("to", "")
    from_ = request.args.get("from", "")
    base_url = request.base_url
    stream_url = f"{base_url}/static/output.ogg"
    if to and from_:
        client = create_vonage_api_client()
        make_vonage_call(client, to=to, from_=from_, stream_url=stream_url)
        return "audio morse code sent", 200
    return "Query parameter 'to' and 'from' should be a valid phone number", 400


@app.route("/answered")
def call_answered():
    return "call is answered"


if __name__ == '__main__':
    app.run()
