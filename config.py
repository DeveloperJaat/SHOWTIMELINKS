# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "Your Api Id"))
API_HASH = os.environ.get("API_HASH", "Your Api Hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "Bot Token")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://bot:bot@cluster0.nbmphsx.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1314385986")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002118263898")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Showtimelinks") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
