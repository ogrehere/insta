from telethon import TelegramClient, events

# Configure the Telegram client
api_id = "5994204"
api_hash = "1c40c54693e2cdbe51f90a152ed1bd5f"
bot_token = "7044443623:AAGSsD9LOw3_u1BGqbgjy2Tuvoiy2mTOsCo"

# Initialize the Telegram client
client = TelegramClient("my_bot", api_id, api_hash).start(bot_token=bot_token)

# Define the channel link
channel_link = "https://t.me/wifisjcj227"

# Global variable to keep track of the current video index
current_video_index = 0

# Function to get videos from channel
# Function to get videos from channel
def get_channel_videos():
    # List of video URLs
    video_urls = [
                  "https://t.me/wifisjcj227/*"
                 ]
    return video_urls


# Event handler for the "/start" command
@client.on(events.NewMessage(pattern='/start'))
async def start_command(event):
    await event.respond("Press the button to get a video from the channel.")

# Event handler for "/get_video" command
@client.on(events.NewMessage(pattern='/get_video'))
async def get_video_command(event):
    global current_video_index
    videos = get_channel_videos()
    if current_video_index < len(videos):
        video_url = videos[current_video_index]
        await event.respond(file=video_url)
        current_video_index += 1
    else:
        await event.respond("No more videos available.")


# Event handler for button clicks
@client.on(events.CallbackQuery)
async def callback_query(event):
    global current_video_index
    if event.data.decode() == "get_video":
        videos = get_channel_videos()
        if current_video_index < len(videos):
            video = videos[current_video_index]
            await event.respond(file=video)
            current_video_index += 1
        else:
            await event.respond("No more videos available.")

# Start the client
client.run_until_disconnected()
