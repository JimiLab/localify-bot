import yaml

config = yaml.safe_load(open("../conf.yaml"))

BOT_TOKEN = config["discord"]["token"]
GUILD_ID = int(config["discord"]["guild-id"])
APPLICATION_ID = config["discord"]["application-id"]
ARTIST_CITY_CHANNEL = config["discord"]["artist-city-channel"]
MODEL_TRAINED_CHANNEL = config["discord"]["model-trained-channel"]

API_HOST = config["api"]["host"]
API_PORT = int(config["api"]["port"])

BACKEND_TOKEN = config["backend"]["token"]
