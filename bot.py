from telethon import TelegramClient, events

# Configure the Telegram client
api_id = "5994204"
api_hash = "1c40c54693e2cdbe51f90a152ed1bd5f"
bot_token = "6707583022:AAF6EyMsuhRODoZguT9XwGcPkOAXwteeijQ"

# Initialize the Telegram client
client = TelegramClient("my_bot", api_id, api_hash).start(bot_token=bot_token)

# Global variable to keep track of the current video index
current_video_index = 0

# Function to get videos from channel
async def get_channel_videos():
    # Define the channel link
    channel_link = "https://t.me/wifisjcj227"
    # Initialize an empty list to store video URLs
    video_urls = []
    # Get the channel entity
    entity = await client.get_entity(channel_link)
    # Iterate over messages in the channel and extract video URLs
    async for message in client.iter_messages(entity):
        if message.media and hasattr(message.media, 'document') and message.media.document.mime_type == 'video/mp4':
            # Get the download URL for the video
            download_url = await client.download_media(message.media)
            video_urls.append(download_url)
    return video_urls


# Event handler for "/get_video" command
@client.on(events.NewMessage(pattern='/get_video'))
async def get_video_command(event):
    global current_video_index
    videos = await get_channel_videos()
    if current_video_index < len(videos):
        video_url = videos[current_video_index]
        await event.respond(file=video_url)
        current_video_index += 1
    else:
        await event.respond("No more videos available.")

# Start the client
client.run_until_disconnected()
