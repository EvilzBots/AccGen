import os

class Config(object):
    TOKEN = os.environ.get("TOKEN", None)
    API_HASH = os.environ.get("API_HASH", None)
    APP_ID = int(os.environ.get("APP_ID", 6))
    PRV_CHAT = int(os.environ.get("PRV_CHAT", False))
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    CHANNEL_URL = os.environ.get("CHANNEL_URL", None)
    CHANNEL_US = os.environ.get("CHANNEL_US", None)
