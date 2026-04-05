# AnnieXMusic / AnnieXMedia — Telegram Music Bot

A Telegram music bot for high-quality streaming in group voice chats. Supports YouTube, Spotify, Apple Music, Resso, and SoundCloud.

## Tech Stack

- **Language**: Python 3.12
- **Telegram Framework**: Pyrogram (MTProto API) + Py-TgCalls (voice chat streaming)
- **Database**: MongoDB (async via `motor`)
- **Media**: yt-dlp, ffmpeg, OpenCV, Pillow
- **Search**: youtube-search-python (with custom async shim at `youtubesearchpython/aio.py`)

## Project Structure

```
AnnieXMedia/          Main bot package
  core/               Bot client, userbot, call controller, MongoDB
  plugins/            Feature modules (admins, bot, play, tools, etc.)
  platforms/          Platform APIs (YouTube, Spotify, Apple, Resso, SoundCloud)
  utils/              Helpers, database wrappers, stream management
  mongo/              MongoDB model wrappers
  assets/             Static assets (fonts, images)
strings/              Multi-language YAML support
config.py             Central configuration (reads from env vars / .env)
```

## Running

The bot runs as a console workflow: `python3 -m AnnieXMedia`

## Required Secrets (Replit Secrets)

| Key | Description |
|-----|-------------|
| `API_ID` | Telegram API ID from https://my.telegram.org |
| `API_HASH` | Telegram API Hash |
| `BOT_TOKEN` | Bot token from @BotFather |
| `OWNER_ID` | Your numeric Telegram user ID |
| `STRING_SESSION` | Pyrogram session string for the assistant userbot |
| `MONGO_DB_URI` | MongoDB connection string |
| `LOGGER_ID` | Numeric ID of the Telegram group/channel for logging |

## Key Fixes Applied During Import

1. **requirements.txt**: Replaced private GitHub dependency (`CertifiedCoders/youtube-search-python`) with public `youtube-search-python` PyPI package.
2. **Async shim**: Added `youtubesearchpython/aio.py` compatibility layer (the installed package lacks the `aio` submodule).
3. **database.py**: Added missing `is_autoplay_on`, `autoplay_on`, `autoplay_off` functions.
4. **start.py**: Fixed broken `InlineKeyboardMarkup` syntax (duplicate list index).
5. **__main__.py**: Made voice-chat test at startup non-fatal (warns instead of exiting if log group has no active voice chat).
6. **System deps**: Installed `xorg.libxcb` and related X11 libraries needed by OpenCV, plus `ffmpeg`.
