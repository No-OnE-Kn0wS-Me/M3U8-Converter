import logging
from translation import Translation
from m3u8 import BLACKLIST_USERS
from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "LEGEND User", "Unlimited")
    return expires_at


@Client.on_message(Filters.command(["help", "about"]))
async def help_user(bot, update):
    # LOGGER.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(Filters.command(["me", "checkme"]))
async def get_me_info(bot, update):
    if update.from_user.id in BLACKLIST_USERS:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.BLACKLIST_TEXT,
            parse_mode="markdown",
            reply_to_message_id=update.message_id,
            disable_web_page_preview=True
        )
    
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text="**You don't have any Restrictions Applied to your Account**\n Telegram ID : `{}`\n\n__If you Enjoyed this BOT, Kindly Donate__",
            parse_mode="markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Donate ❤️', url='https://www.patreon.com/WhySooSerious'),
                    ]
                ]
            ),
            reply_to_message_id=update.message_id,
            disable_web_page_preview=True
        )

@Client.on_message(Filters.command(["start"]))
async def start(bot, update):
    # LOGGER.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Source 😒', url='https://t.me/WhySooSerious/7'),
                    InlineKeyboardButton('Other BOTs', url='https://t.me/WhySooSerious/6')
                ],
                [
                    InlineKeyboardButton('Report Bugs', url='https://t.me/WhySooSerious')
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )
    bot.send_message(
        chat_id=-1001290702235,
        text=f"[{update.from_user.first_name}](tg://user?id={bot.message.chat.id}) Started The Bot",
        parse_mode="markdown"
    )


@Client.on_message(Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # LOGGER.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Donate ❤️', url='https://www.patreon.com/WhySooSerious'),
                ]
            ]
        ),
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )

@Client.on_message(Filters.command(["anime"]))
async def anime(bot, update):
    # LOGGER.info(update)
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/daee5afb23399c9c536e2.jpg",
        caption="__Looking for a Best Place for watching AD-FREE Anime?__\n\nClick on the Button Below and and Search.\n\n__If you need the Episode as a Telegram Video,__\n__Copy the M3U8 link and Paste it here to get it as a Telegram Video__",
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Anime Stream BOT', url='https://t.me/Anime_Stream_BOT'),
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )


#    await bot.send_message(
#        chat_id=update.chat.id,
#        text="Looking for a Best Place for watching AD-FREE Anime?\n\nClick on the Button Below and and Search.\n\nIf you need the Episode as a Telegram Video,\nCopy the M3U8 link and Paste it here to get it as a Telegram Video",
#        parse_mode="markdown",
#        reply_markup=InlineKeyboardMarkup(
#           [
#                [
#                    InlineKeyboardButton('Anime Stream BOT', url='https://t.me/Anime_Stream_BOT'),
#                ]
#            ]
#        ),
#        reply_to_message_id=update.message_id
#    )