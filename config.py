# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("39682304", ""))
API_HASH = getenv("da5b28e3e90a7d49b930a89f436fc327", "")
BOT_TOKEN = getenv("8570595039:AAE4nHTU4x0JaPK4HQvj84SK6yME2RXsXkU", "")
OWNER_ID = list(map(int, getenv("7365576089", "").split()))
MONGO_DB = getenv("mongodb+srv://valanamrajitsinh9_db_user:1gFCstnZ9Zjie1d7@cluster0.s0sv5ha.mongodb.net/?appName=Cluster0", "")
LOG_GROUP = getenv("7365576089", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
