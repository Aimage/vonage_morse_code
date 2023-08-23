import os
from dotenv import load_dotenv

load_dotenv()

SOUND_BASE_PATH = os.getenv("SOUND_BASE_PATH", 'morse_sound_files/')
APPLICATION_ID = os.getenv("APPLICATION_ID", "")
PRIVATE_KEY = os.getenv("PRIVATE_KEY", "")
