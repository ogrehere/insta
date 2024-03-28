from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Create a Pyrogram Client
api_id = "5994204"
api_hash = "1c40c54693e2cdbe51f90a152ed1bd5f"
bot_token = "6707583022:AAHk4Z_bdd22vAuyOe7CVoGiSPVQy-y1vSU"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define the channel link
channel_link = "https://t.me/wifisjcj227"

# Global variable to keep track of the current video index
current_video_index = 0

# Function to get videos from channel
def get_channel_videos():
    # Code to scrape videos from the channel
    # Replace this with your own scraping logic
    videos = ["video1.mp4", "video2.mp4", "video3.mp4"]
    return videos

# Command handler
@app.on_message(filters.command(["start"]))
def start_command(client, message):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Get Video", callback_data="get_video")]
    ])
    message.reply_text("Press the button to get a video from the channel.", reply_markup=reply_markup)

# Callback query handler
@app.on_callback_query()
def callback_query(client, callback_query):
    global current_video_index
    if callback_query.data == "get_video":
        videos = get_channel_videos()
        if current_video_index < len(videos):
            video = videos[current_video_index]
            client.send_video(callback_query.message.chat.id, video)
            current_video_index += 1
        else:
            client.send_message(callback_query.message.chat.id, "No more videos available.")

# Start the bot
app.run()
