import pyrogram 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import phonenumbers
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder



# Replace with your actual credentials
API_ID = 5994204  
API_HASH = "1c40c54693e2cdbe51f90a152ed1bd5f" 
BOT_TOKEN = "7044443623:AAGSsD9LOw3_u1BGqbgjy2Tuvoiy2mTOsCo"

app = pyrogram.Client("my_info_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Modify the start command to include buttons with images
@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "Welcome! Send a phone number to get information about it.\nExample: 919876543210"
    )

@app.on_message(filters.private & filters.text)
async def process_number(client, message):
    try:
        phone_number = phonenumbers.parse(message.text)
        geolocator = Nominatim(user_agent="my_info_bot")
        location = geolocator.geocode(phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164))

        if location:
            timezone = TimezoneFinder().timezone_at(lng=location.longitude, lat=location.latitude)
            await message.reply_text(
                f"🔍 Number Information 🔍\n"
                f"📞 Number: {message.text}\n"
                f"👤 Name: (Not always available)\n"
                f"🌍 Country: {geolocator.country_name}\n"
                f"⏰ TimeZone: {timezone}"
            )
        else:
            await message.reply_text("Location information not available for this phone number.")

    except phonenumbers.phonenumberutil.NumberParseException:
        await message.reply_text("Invalid phone number format. Please provide a valid number.")


app.run()
