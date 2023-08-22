import vonage
from config import APPLICATION_ID, PRIVATE_KEY


def create_vonage_api_client():
    client = vonage.Client(application_id=APPLICATION_ID,
                           private_key=PRIVATE_KEY)
    return client


def make_vonage_call(client,
                     to='14843331234',
                     from_="14843335555",
                     stream_url=''):
    stream_url = stream_url
    response = client.voice.create_call({
        'to': [{
            'type': 'phone',
            'number': to
        }],
        'from': {
            'type': 'phone',
            'number': from_
        },
        'answer_url': ['https://example.com/answer']
    })
    client.voice.send_audio(response['uuid'], stream_url=[stream_url])
