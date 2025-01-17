from os import environ 

class Config:
    API_ID = environ.get("API_ID", "12188448")
    API_HASH = environ.get("API_HASH", "db8f6f60dec66df3b05d886ee922eecb")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7580287617:AAF1moeZMpXLORWTKZ36y9kWdfI-Jaus_kA") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6118218269').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
