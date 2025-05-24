from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from faker import Faker

faker = Faker()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Commands", callback_data="button_1"),
         InlineKeyboardButton("Info", callback_data="button_2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select an action:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    HELP = """Commands for generating fake:

/name - Name
/first_name - First Name
/last_name - Last Name
/prefix - Prefix
/suffix - Suffix
/date_of_birth - Date of Birth
/address - Address
/street_address - Street Address
/city - City
/state - State
/zipcode - Zipcode
/country - Country
/country_code - Country Code
/latitude - Latitude
/longitude - Longitude
/coordinate - Coordinate
/phone_number - Phone Number
/email - Email
/safe_email - Safe Email
/free_email - Free Email
/domain_name - Domain Name
/url - URL
/credit_card_number - Credit Card Number
/credit_card_expire - Credit Card Expire
/credit_card_full - Credit Card Full
/currency_name - Currency Name
/currency_code - Currency Code
/company - Company
/company_suffix - Company Suffix
/job - Job
/date - Date
/time - Time
/datetime - Datetime
/iso8601 - ISO8601
/date_this_year - Date This Year
/time_delta - Time Delta
/word - Word
/words - Words
/text - Text
/paragraph - Paragraph
/sentences - Sentences
/ascii_free_email - Ascii Free Email
/ipv4 - IPv4
/ipv6 - IPv6
/mac_address - Mac Address
/file_name - File Name
/file_path - File Path
/mime_type - MIME Type
/random_digit - Random Digit
/random_int - Random Int
/random_number - Random Number
/password - Password
"""

    INFO = "This is a bot for generating false information that uses the Python module faker.\n\nDeveloper: @MaxKostash"

    if query.data == "button_1":
        keyboard = [[InlineKeyboardButton("Back", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(HELP, reply_markup=reply_markup)
    elif query.data == "button_2":
        keyboard = [[InlineKeyboardButton("Back", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(INFO, reply_markup=reply_markup)
    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("Commands", callback_data="button_1"),
             InlineKeyboardButton("Info", callback_data="button_2")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Select an action:", reply_markup=reply_markup)

async def name(update: Update, context:
               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.name())

async def first_name(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.first_name())

async def last_name(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.last_name())

async def prefix(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.prefix())

async def suffix(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.suffix())

async def date_of_birth(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.date_of_birth())

async def address(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.address())

async def street_address(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.street_address())

async def city(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.city())

async def state(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.state())

async def zipcode(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.zipcode())

async def country(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.country())

async def country_code(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.country_code())

async def latitude(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.latitude())

async def longitude(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.longitude())

async def coordinate(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.coordinate())

async def phone_number(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.phone_number())

async def email(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.email())

async def safe_email(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.safe_email())

async def free_email(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.free_email())

async def domain_name(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.domain_name())

async def url(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.url())

async def credit_card_numder(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.credit_card_number())

async def credit_card_expire(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.credit_card_expire())

async def credit_card_full(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.credit_card_full())

async def currency_name(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.currency_name())

async def currency_code(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.currency_code())

async def company(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.company())

async def company_suffix(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.company_suffix())

async def job(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.job())

async def date(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.date())

async def time(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.time())

async def date_time(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.date_time())

async def iso8601(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.iso8601())

async def date_this_year(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.date_this_year())

async def time_delta(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.time_delta())

async def word(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.word())

async def words(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.words())

async def text(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.text())

async def paragraph(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.paragraph())

async def sentences(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.sentences())

async def ascii_free_email(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.ascii_free_email())

async def ipv4(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.ipv4())

async def ipv6(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.ipv6())

async def mac_address(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.mac_address())

async def file_name(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.file_name())

async def file_path(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.file_path())

async def mime_type(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.mime_type())

async def random_digit(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.random_digit())

async def random_int(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.random_int())

async def random_number(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.random_number())

async def password(update: Update, context:                               ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(faker.password())

def add_fake_command_handlers(application):
    commands = {
        "name": faker.name,
        "first_name": faker.first_name,
        "last_name": faker.last_name,
        "prefix": faker.prefix,
        "suffix": faker.suffix,
        "date_of_birth": faker.date_of_birth,
        "address": faker.address,
        "street_address": faker.street_address,
        "city": faker.city,
        "state": faker.state,
        "zipcode": faker.zipcode,
        "country": faker.country,
        "country_code": faker.country_code,
        "latitude": faker.latitude,
        "longitude": faker.longitude,
        "coordinate": faker.coordinate,
        "phone_number": faker.phone_number,
        "email": faker.email,
        "safe_email": faker.safe_email,
        "free_email": faker.free_email,
        "domain_name": faker.domain_name,
        "url": faker.url,
        "credit_card_number": faker.credit_card_number,
        "credit_card_expire": faker.credit_card_expire,
        "credit_card_full": faker.credit_card_full,
        "currency_name": faker.currency_name,
        "currency_code": faker.currency_code,
        "company": faker.company,
        "company_suffix": faker.company_suffix,
        "job": faker.job,
        "date": faker.date,
        "time": faker.time,
        "datetime": faker.date_time,
        "iso8601": faker.iso8601,
        "date_this_year": faker.date_this_year,
        "time_delta": faker.time_delta,
        "word": faker.word,
        "words": faker.words,
        "text": faker.text,
        "paragraph": faker.paragraph,
        "sentences": faker.sentences,
        "ascii_free_email": faker.ascii_free_email,
        "ipv4": faker.ipv4,
        "ipv6": faker.ipv6,
        "mac_address": faker.mac_address,
        "file_name": faker.file_name,
        "file_path": faker.file_path,
        "mime_type": faker.mime_type,
        "random_digit": faker.random_digit,
        "random_int": faker.random_int,
        "random_number": faker.random_number,
        "password": faker.password,
    }

    for command, func in commands.items():
        async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE, func=func):
            await update.message.reply_text(func())
        application.add_handler(CommandHandler(command, handler))

def main():

    application = Application.builder().token("token").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    add_fake_command_handlers(application)

    application.run_polling()

if __name__ == "__main__":
    main()