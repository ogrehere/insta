from telethon.sync import TelegramClient, events
import requests
import os

# Telegram bot credentials
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

# Initialize Telegram client
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Define a function to download Instagram videos
def download_instagram_video(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            if 'video' in content_type:
                file_name = 'instagram_video.mp4'
                with open(file_name, 'wb') as f:
                    f.write(response.content)
                return file_name
            else:
                return "Provided URL is not for a video."
        else:
            return "Failed to download the video."
    except Exception as e:
        return str(e)

# Define a handler for incoming messages
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Welcome! Please send me the URL of the Instagram video you want to download.')

# Define a handler for incoming messages containing Instagram video URLs
@client.on(events.NewMessage)
async def handle_message(event):
    if event.message.text.startswith('https://www.instagram.com/p/'):
        video_url = event.message.text
        file_path = download_instagram_video(video_url)
        if file_path:
            await event.respond('Here is your Instagram video:', file=open(file_path, 'rb'))
            os.remove(file_path)
        else:
            await event.respond('Failed to download the Instagram video.')
    else:
        await event.respond('Please provide a valid Instagram video URL.')

# Start the bot
client.run_until_disconnected()
