#
# Copyright (C) 2021-2023 by ArchBots@Github, < https://github.com/ArchBots >.
#
# This file is part of < https://github.com/ArchBots/ArchMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/ArchBots/ArchMusic/blob/master/LICENSE >
#
# All rights reserved.
#

from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from ArchMusic import app
from ArchMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Gizli Grup"
        logger_text = f"""
**{MUSIC_BOT_NAME} Play Log**

**Grup🫧:** {message.chat.title} [`{message.chat.id}`]
**Üye Sayısı🫧: 💡{sayı}**
**Kullanıcı Adı🫧:** @{message.from_user.username}
**Kullanıcı ID🫧:** `{message.from_user.id}`
**Grup Link🫧:** {chatusername}

**Toplam Grup Sayısı: 💡{toplamgrup}**

**Aktif Ses: 💡{aktifseslisayısı}**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
