import pyrogram
from pyrogram.types import filters, InlineKeyboardButton, InlineKeyboardMarkup
import phonenumbers
import geocoder

# Replace with your actual credentials
API_ID = 5994204  
API_HASH = "1c40c54693e2cdbe51f90a152ed1bd5f" 
BOT_TOKEN = "7044443623:AAGSsD9LOw3_u1BGqbgjy2Tuvoiy2mTOsCo"

app = pyrogram.Client("my_info_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Modify the start command to include buttons with images
@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    joined = await check_required_channels(client, message.chat.id)

    if not joined:
        # Create InlineKeyboardMarkup with buttons and images
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Channel 1",
                        url="https://t.me/VoidexTg",
                        callback_data="channel1"
                    ),
                    InlineKeyboardButton(
                        text="Channel 2",
                        url="https://t.me/EsportLeaker",
                        callback_data="channel2"
                    )
                ]
            ]
        )

        await message.reply_text(
            "You Must Join All Our Channels to Access This Bot",
            reply_markup=keyboard
        )
    else:
        await message.reply_text(
            "Welcome! Send a phone number to get information about it.\nExample: 919876543210"
        )

@app.on_message(filters.private & filters.text)
async def process_number(client, message):
    try:
        phone_number = phonenumbers.parse(message.text)

        info = phonenumbers.geocoder.description_for_number(phone_number, "en")
        carrier = phonenumbers.carrier.name_for_number(phone_number, "en")
        g = geocoder.timezone(info)

        await message.reply_photo(
            photo="https://telegra.ph/file/f0b21cd8808d4fc97eb62.png",
            caption=f"🔍 Number Information 🔍\n"
                    f"📞 Number: {message.text}\n"
                    f"👤 Name: (Not always available)\n"
                    f"📡 Carrier: {carrier}\n"
                    f"🌍 Country: {info}\n"
                    f"⏰ TimeZone: {g.zone}"
        )

    except phonenumbers.phonenumberutil.NumberParseException:
        await message.reply_text("Invalid phone number format. Please provide a valid number.")


async def check_required_channels(client, user_id):
    for channel in REQUIRED_CHANNELS:
        chat_member = await client.get_chat_member(channel, user_id)
        if chat_member.status != "member":
            return False
    return True


app.run()
