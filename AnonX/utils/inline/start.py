from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="•✯ ✗ ᴀᴅᴅ ᴍᴇ ᴍᴇʀɪ ᴊᴀᴀɴ ✯• ✗",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=="•❀ ʜᴇʟᴘ & ᴄᴍᴅs ❀•",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="•✵ sᴇᴛᴛɪɴɢs ✵•", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="•✯ ✗ ᴀᴅᴅ ᴍᴇ ᴍᴇʀɪ ᴊᴀᴀɴ ✗ ✯•",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="•❀ ʜᴇʟᴘ & ᴄᴍᴅs ❀•", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text=="•✩ sᴜᴘᴘᴏʀᴛ ✩•", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="•♡︎ ᴅᴇᴠᴇʟᴏᴘᴇʀ ♡︎•", url=f"https://t.me/its_Coder_xD"
            )
        ]
     ]
    return buttons
