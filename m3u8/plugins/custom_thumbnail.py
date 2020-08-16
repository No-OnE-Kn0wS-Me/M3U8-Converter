import logging
import os
from pyrogram import (
    Client,
    Filters
)
from m3u8 import (
    DOWNLOAD_LOCATION
)
# the Strings used for this "thing"
from translation import Translation


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(Filters.photo)
async def save_photo(bot, update):
    # received single photo
    download_location = os.path.join(
        DOWNLOAD_LOCATION,
        str(update.from_user.id) + ".jpg"
    )
    await bot.download_media(
        message=update,
        file_name=download_location
    )
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.SAVED_CUSTOM_THUMB_NAIL,
        reply_to_message_id=update.message_id
    )


@Client.on_message(Filters.command(["deletethumbnail"]))
async def delete_thumbnail(bot, update):
    download_location = os.path.join(
        DOWNLOAD_LOCATION,
        str(update.from_user.id)
    )
    try:
        os.remove(download_location + ".jpg")
        # os.remove(download_location + ".json")
        bot.send_message(
        chat_id=update.chat.id,
        text=Translation.DEL_ETED_CUSTOM_THUMB_NAIL,
        reply_to_message_id=update.message_id
    )