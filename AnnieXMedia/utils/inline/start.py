# Authored By II_YOUR_MADARA_DEFAULTER_II © 2025
from pyrogram.types import InlineKeyboardButton

import config
from AnnieXMedia import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ✚",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="👑 ᴅᴇᴠᴇʟᴏᴘᴇʀ",
                user_id=config.OWNER_ID,
            ),
            InlineKeyboardButton(
                text="🖥️ ʏᴛ-ᴀᴘɪ",
                callback_data="ytapi_ping",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📢 ᴜᴘᴅᴀᴛᴇ ↗",
                url=config.SUPPORT_CHANNEL,
            ),
            InlineKeyboardButton(
                text="💬 sᴜᴘᴘᴏʀᴛ ↗",
                url=config.SUPPORT_CHAT,
            ),
        ],
        [
            InlineKeyboardButton(
                text="❓ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs",
                callback_data="open_help",
            ),
        ],
    ]
    return buttons
