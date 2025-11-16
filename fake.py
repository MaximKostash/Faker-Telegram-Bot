import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from faker import Faker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

faker = Faker("ru_RU")

COMMANDS = [
    ("Name", "name"),
    ("First Name", "first_name"),
    ("Last Name", "last_name"),
    ("Prefix", "prefix"),
    ("Suffix", "suffix"),
    ("Date of Birth", "date_of_birth"),
    ("Address", "address"),
    ("Street Address", "street_address"),
    ("City", "city"),
    ("State", "state"),
    ("Zipcode", "zipcode"),
    ("Country", "country"),
    ("Country Code", "country_code"),
    ("Latitude", "latitude"),
    ("Longitude", "longitude"),
    ("Coordinate", "coordinate"),
    ("Phone Number", "phone_number"),
    ("Email", "email"),
    ("Safe Email", "safe_email"),
    ("Free Email", "free_email"),
    ("Domain Name", "domain_name"),
    ("URL", "url"),
    ("Credit Card Number", "credit_card_number"),
    ("Credit Card Expire", "credit_card_expire"),
    ("Credit Card Full", "credit_card_full"),
    ("Currency Name", "currency_name"),
    ("Currency Code", "currency_code"),
    ("Company", "company"),
    ("Company Suffix", "company_suffix"),
    ("Job", "job"),
    ("Date", "date"),
    ("Time", "time"),
    ("ISO8601", "iso8601"),
    ("Date This Year", "date_this_year"),
    ("Time Delta", "time_delta"),
    ("Word", "word"),
    ("Text", "text"),
    ("Paragraph", "paragraph"),
    ("Ascii Free Email", "ascii_free_email"),
    ("IPv4", "ipv4"),
    ("IPv6", "ipv6"),
    ("Mac Address", "mac_address"),
    ("File Name", "file_name"),
    ("File Path", "file_path"),
    ("MIME Type", "mime_type"),
    ("Random Digit", "random_digit"),
    ("Random Int", "random_int"),
    ("Random Number", "random_number"),
    ("Password", "password"),
]

PAGE_SIZE = 8

def get_commands_keyboard(page: int = 0):
    total_pages = (len(COMMANDS) + PAGE_SIZE - 1) // PAGE_SIZE
    page_commands = COMMANDS[page * PAGE_SIZE : (page + 1) * PAGE_SIZE]
    keyboard = []
    row = []
    for idx, (label, cmd) in enumerate(page_commands, 1):
        row.append(InlineKeyboardButton(label, callback_data=f"cmd_{cmd}_p{page}"))
        if idx % 2 == 0:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton("⬅️ Previous", callback_data=f"page_{page-1}"))
    if page < total_pages - 1:
        nav_buttons.append(InlineKeyboardButton("Next ➡️", callback_data=f"page_{page+1}"))
    if nav_buttons:
        keyboard.append(nav_buttons)
    keyboard.append([InlineKeyboardButton("Main menu", callback_data="back")])
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        keyboard = [
            [InlineKeyboardButton("Commands", callback_data="button_1"),
             InlineKeyboardButton("Info", callback_data="button_2")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        if update.message:
            await update.message.reply_text("Select an action:", reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error in start: {e}")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if not query:
        return
    try:
        await query.answer()
        INFO = (
            "This bot generates various fake information.\n\n"
            "Developer: @MaxKostash"
        )

        if query.data == "button_1":
            await query.edit_message_text("Choose a data category:", reply_markup=get_commands_keyboard(0))
        elif query.data == "button_2":
            keyboard = [[InlineKeyboardButton("Main menu", callback_data="back")]]
            await query.edit_message_text(INFO, reply_markup=InlineKeyboardMarkup(keyboard))
        elif query.data == "back":
            keyboard = [
                [InlineKeyboardButton("Commands", callback_data="button_1"),
                 InlineKeyboardButton("Info", callback_data="button_2")]
            ]
            await query.edit_message_text("Select an action:", reply_markup=InlineKeyboardMarkup(keyboard))
        elif query.data.startswith("page_"):
            page = int(query.data.split("_")[1])
            await query.edit_message_text("Choose a data category:", reply_markup=get_commands_keyboard(page))
        elif query.data.startswith("cmd_"):
            parts = query.data.split("_")
            cmd = "_".join(parts[1:-1])
            page = int(parts[-1][1:])
            value = await generate_fake_data(cmd)
            await query.edit_message_text(str(value), reply_markup=get_commands_keyboard(page))
    except Exception as e:
        logger.error(f"Error in button_handler: {e}")
        await query.edit_message_text("An error occurred. Please try again later.")

async def generate_fake_data(cmd):
    try:
        func = getattr(faker, cmd, None)
        if not func or not callable(func):
            return "Unknown command."
        value = func()
        if isinstance(value, list):
            return ", ".join(str(x) for x in value)
        return value
    except Exception as e:
        logger.error(f"Error in generate_fake_data: {e}")
        return "Error while generating data."

def add_fake_command_handlers(application):
    for _, cmd in COMMANDS:
        async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE, cmd=cmd):
            try:
                value = await generate_fake_data(cmd)
                if update.message:
                    await update.message.reply_text(str(value))
            except Exception as e:
                logger.error(f"Error in handler for {cmd}: {e}")
        application.add_handler(CommandHandler(cmd, handler))

def main():
    application = Application.builder().token("7069915868:AAHpZxvDA1_4ZTmPlVDSvVD0n2asQzUpBmM").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    add_fake_command_handlers(application)
    application.run_polling()

if __name__ == "__main__":
    main()