from os import environ 

class Config:
    API_ID = environ.get("API_ID", "27494535")
    API_HASH = environ.get("API_HASH", "52210cf4440a4a2b816ed1bcad615d4d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7082109889:AAHdY0TroWFKjd8gyZGtpzNP8gXS4_sqrWk") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://kepipot979:kepipot979@cluster0.cm8t1fp.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5601277336').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
