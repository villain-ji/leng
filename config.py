import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "26064438"))
API_HASH = getenv("API_HASH", "9b4f90f3b1cddcc25cd230fc2c03c1a4")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7398714280:AAHZcLX4yQNPxnwcv4IbdKFC3pFcVJL1stQ")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://manoranjanhor43:somuxd@manoranjan.wsglmdq.mongodb.net/?retryWrites=true&w=majority&appName=Manoranjan")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002046320443))

OWNER_ID = int(getenv("OWNER_ID", 7520092354))

OWNER = int(getenv("OWNER", 7520092354))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","lenged")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HK543fklqxgt66hvxf")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/villain-ji/leng",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/The_Incricible")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Zoyu_support")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION","BQGNtjYAZ4SbjBAandqNdAlC_dw2IYtmV-yYdTa7R2JxilhY0ca1CZ4cD0OEfTaJlPuWC5lsmLYpBkbHs8w-zPaXB_meEhdbT7ClBfz9KQ-gBK90WeTV5zNpIOz9mHztYFIiUWC3_rFuRNex0SOvv0q3ohT9gpB-9Ei3V8L1whNTNmVowjSC3j8_q7w8oYwa9XAivr5t3a25mUyd5HvfvAYVDWS6v9M8yHnWg-LckzrffdOZp3rD9ugbTtubxsBeRaj_rkGjZ964g9aZhk6pUGiwxp1WnJhuUVIJn1NQzontACdpln-gFI5QvN5z3ZH1fzOfYraAkrthUVv-CO9tVY2afJRN9wAAAAHa0RexAA")
STRING2 = getenv("STRING_SESSION2","BQGByu8ApZChFIO591AvdVztmQFZ4nLo1BnuBCf83itAPoL1QNhF6qlDwVhAP4cGcTcVX1MRuphTcKzv8k1My9cKHrHB_ZcYzv6KH6corcrbml7rNaZlHm09ddmu-kOC7GiQUgZY26YI9Ifgd64fYY_KzgDAxawMTcqDDMLA7R58UdA0VJC8ufe6hbJDgeJ_mmCPI1MfRumgzYExWL0REe79azlPTvHwAXVJDicP3HdGJI7xQvpOD5M_vfkU6SsVgcrAO-E6RHoy8lJ_cGw6QL_I6bHS20pNcx7GyAHNH62PWg-0pslSDtTW1JNTWKMUcWlx35lJB5gfHUZpBB95m0DU0xqJAAAAAAHoMT_KAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/4e68b6d15e042249fb284.png")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/b37803a767b15e939513d.png")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://telegra.ph/file/4e68b6d15e042249fb284.png")
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
