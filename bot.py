from telethon.sync import TelegramClient, events
import os
import instaloader

# Telegram bot credentials
api_id = "5994204"
api_hash = "1c40c54693e2cdbe51f90a152ed1bd5f"
bot_token = "6707583022:AAEahTtTAlqL0ujzwbkNNSLGorFlBs63CRQ"

# Initialize Telegram client
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Define a function to download Instagram videos
def download_instagram_video(url):
    try:
        # Create an instaloader instance
        loader = instaloader.Instaloader()

        # Get post information
        post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])

        # Get video URL
        video_url = post.video_url

        # Download the video
        file_name = 'instagram_video.mp4'
        loader.download_post(post, target=file_name)
        
        return file_name

    except Exception as e:
        return str(e)

# Define a handler for incoming messages
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Welcome! Please send me the URL of the Instagram video you want to download.')

# Define a handler for incoming messages containing Instagram video URLs
@client.on(events.NewMessage)
async def handle_message(event):
    if event.message.text.startswith('https://www.instagram.com/reel/'):
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
