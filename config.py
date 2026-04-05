# Authored By Certified Coders © 2025
import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ── Core bot config ────────────────────────────────────────────────────────────
API_ID = int(getenv("API_ID", 35411328 ))
API_HASH = getenv("API_HASH", "4c8d3c8f5d3483296f5fb530ea2cfcc6")
# 🛠️ FIXED: Removed variable name from inside token
BOT_TOKEN = getenv("BOT_TOKEN", "8776563274:AAHnLHiwJ9ZmrztOfKn6ldEpB6Y97EOFQ4Y")

OWNER_ID = int(getenv("OWNER_ID", 8441236350))
OWNER_USERNAME = getenv("OWNER_USERNAME", "II_YOUR_MADARA_DEFAULTER_II")
BOT_USERNAME = getenv("BOT_USERNAME", "RADHA_MUSIC_GMS_bot")
BOT_NAME = getenv("BOT_NAME", "ʀᴀᴅʜᴀ ᴍᴜsɪᴄ 🎧✨")
ASSUSERNAME = getenv("ASSUSERNAME", "RADHA_X_ASSITANT")

# ── Database & logging ─────────────────────────────────────────────────────────
# 🛠️ FIXED: Proper getenv syntax for MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://bsdk:betichod@cluster0.fgj1r9z.mongodb.net/?retryWrites=true&w=majority")
LOGGER_ID = int(getenv("LOGGER_ID", -1003774441740))

# ── Limits (durations in min/sec; sizes in bytes) ──────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1200"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "157286400"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1288490189"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "30"))

# ── External APIs ──────────────────────────────────────────────────────────────
# 🛠️ FIXED: Proper getenv syntax
COOKIE_URL = getenv("COOKIE_URL", "https://files.catbox.moe/xh6f12.txt")  # required (paste link)
API_URL = getenv("https://api.nexgenbots.xyz")        # optional
VIDEO_API_URL = getenv("https://api.video.nexgenbots.xyz")  # optional
API_KEY = getenv("NxGBNexGenBots67b7b6")        # optional
DEEP_API = getenv("DEEP_API")      # optional

# ── Hosting / deployment ───────────────────────────────────────────────────────
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ── Git / updates ──────────────────────────────────────────────────────────────
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ragini19854-prog/Kya-pata-re-bisi")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")  # needed if repo is private

# ── Support links ──────────────────────────────────────────────────────────────
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+Imyf3M9TO5k1ODRl")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+dv_rcq5uIXhmMWM1")

# ── Assistant auto-leave ───────────────────────────────────────────────────────
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3600"))

# ── Debug ──────────────────────────────────────────────────────────────────────
DEBUG_IGNORE_LOG = True

# ── Spotify (optional) ─────────────────────────────────────────────────────────
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ── Session strings (optional) ─────────────────────────────────────────────────
# 🛠️ FIXED: This is where the main bug was.
STRING1 = getenv("STRING_SESSION", "BAImFsUAK7WRIm2W0nCAyZRRoujv-ROIXSP90hob3aHymRwxLk4XNsLyNDy0zOcaLUfy2DYPd2wzgND0GJdEudlZlPOoPAnOMer5sqTY4_fCbWfi765RQ7lyXZgCci4EHDjobrsQ7YzXhS5Ij8KSPTV_BilSaNOgc0OcuAMqa_x85c9hONMrlez-flSOTyPoqyHRB3wzkg2INEPhctPcvMCHD5Yl2SfC4eHD0CQbp4KGSXfFiQ8vYNdB262_4_TUqKWpLfqJJeIWL-DNg6OgjHwJJvNzxY-NdAzRiJX_Z6GyM0pybajUq3Q7r1D77NiK5J-Id9ThBGR3g6O9LZN43p3iyrd6DgAAAAH3Iwt-AA")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ── Media assets ───────────────────────────────────────────────────────────────
START_VIDS = [
    "https://files.catbox.moe/15yws0.mp4",
    "https://files.catbox.moe/15yws0.mp4",
    "https://files.catbox.moe/15yws0.mp4",
]
STICKERS = [
    "CAACAgUAAxkBAAMmacNGue06n3Ay8QapEjgbZd0JrA4AAhYOAAIlaXhVylgMfC3EZoMeBA",
    "CAACAgUAAxkBAAMtacNHV4JGC0LMqw8-zNODvPZVcp8AAs0SAALVhnhVcnMpz29EzNUeBA",
]
HELP_IMG_URL = "https://files.catbox.moe/r9c3tn.png"
PING_VID_URL = "https://files.catbox.moe/nsgxzw.mp4"
PLAYLIST_IMG_URL = "https://files.catbox.moe/oh07fz.jpg"
STATS_VID_URL = "https://files.catbox.moe/15yws0.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/nzhqh9.png"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/nzhqh9.png"
STREAM_IMG_URL = "https://files.catbox.moe/nzhqh9.png"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/nzhqh9.png"
YOUTUBE_IMG_URL = "https://files.catbox.moe/nzhqh9.png"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ── Helpers ────────────────────────────────────────────────────────────────────
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

#Bot Introduction Messages ───── #
AYU = ["💞", "🦋", "🔍", "🧪", "⚡️", "🔥", "🎩", "🌈", "🍷", "🥂", "🥃", "🕊️", "🪄", "💌", "🧨"]
AYUV = [
    "┌───── ˹ ᴡєʟᴄᴏᴍє ˼─── ⏤‌‌●\n"
    "┆◍ ʜєʏ, {0} 🥀\n"
    "┆◍ ɪ ᴧϻ ˹•´¯•» 🎀 𝐻𝐼𝒩𝒜𝒯𝒜 𝑀𝒰𝒮𝐼𝒞 🎀 »•¯´• ˼ ♪\n"
    "└─────────────────────•\n\n"
    "𝐇ɪɴᴧᴛᴧ 𝐌ᴜsɪᴄ ♪ ɪs ᴀ ғᴀsᴛ ᴀɴᴅ sᴍᴏᴏᴛʜ ᴍᴜsɪᴄ ʙᴏᴛ 🥀\n\n"
    "➥ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ sᴛʀᴇᴀᴍɪɴɢ\n"
    "➥ sᴜᴘᴇʀ ғᴀsᴛ ᴘʟᴀʏʙᴀᴄᴋ\n"
    "➥ sᴍᴏᴏᴛʜ ᴀᴜᴅɪᴏ sʏsᴛᴇᴍ\n"
    "➥ 24x7 ᴍᴜsɪᴄ sᴜᴘᴘᴏʀᴛ\n\n"
     "─────────────────────•\n"
    "🎧 sᴜᴘᴘᴏʀᴛᴇᴅ ᴘʟᴀᴛғᴏʀᴍs:\n"
    "• ʏᴏᴜᴛᴜʙᴇ\n"
    "• sᴘᴏᴛɪғʏ\n"
    "• ʀᴇssᴏ\n"
    "• ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ\n"
    "• sᴏᴜɴᴅᴄʟᴏᴜᴅ\n\n"
    "─────────────────────•\n"
    "❖ ᴘᴏᴡєʀєᴅ ʙʏ - ᴍᴧᴅᴧʀᴧ\n"
    "─────────────────────•\n"
    "❖ ᴄʟɪᴄᴋ ση ᴛʜє ʜєʟᴩ ʙυᴛᴛση\n"
    "─────────────────────•"
]

# ── Runtime structures ─────────────────────────────────────────────────────────
BANNED_USERS = filters.user()
adminlist, lyrical, autoclean, confirmer = {}, {}, [], {}

# ── Minimal validation ─────────────────────────────────────────────────────────
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")
