from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝗛𝗲𝘆 🤨 {}

Welcome to {}

༆ *SESSION STRENG* comes with many special features in it༆

꧁check all button below to explore every commands of lovely꧂

𖣘 All commands can either be used with / or !.

𖣘 If you facing any issue or find any bugs in any command then you can report it in @STUDY_CHATING .
By @shayari_jok !❤️
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 GENERATE SISOSAN 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 GENERATE SISOSAN 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 GENERATE SISOSAN 🔥", callback_data="generate")],
        [InlineKeyboardButton("🤔  command 🤔", callback_data="help")],
        [InlineKeyboardButton("♥ SPORTS GROUP ♥", url="https://t.me/shayari_jok")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
@Umashankar31
"""
