import logging
from pyrogram import (
    Client,
    CallbackQuery
)
from m3u8 import BLACKLIST_USERS
from m3u8.plugins.youtube_dl_button import youtube_dl_call_back
from m3u8.plugins.dl_button import ddl_call_back
from translation import Translation

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_callback_query()
async def button(bot, update: CallbackQuery):
    if update.from_user.id in BLACKLIST_USERS:
        await update.message.delete()
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.FISHY.format(update.chat.id),
            parse_mode="markdown",
            reply_to_message_id=update.message_id,
            disable_web_page_preview=True
        )
        return
    # LOGGER.info(update)
    # NOTE: You should always answer,
    # but we want different conditionals to
    # be able to answer to differnetly
    # (and we can only answer once),
    # so we don't always answer here.
    await update.answer()

    cb_data = update.data
    if "|" in cb_data:
        await youtube_dl_call_back(bot, update)
    elif "=" in cb_data:
        await ddl_call_back(bot, update)
