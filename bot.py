from telethon import TelegramClient, events
import os

# ... (your API credentials and client setup) ...
api_id = 5994204  
api_hash = '1c40c54693e2cdbe51f90a152ed1bd5f'
bot_token = '7044443623:AAGSsD9LOw3_u1BGqbgjy2Tuvoiy2mTOsCo'

client = TelegramClient('video_scraper_bot', api_id, api_hash)
client.start(bot_token=bot_token)

latest_video_index = {}  # A dictionary to store index per chat

@client.on(events.NewMessage(pattern='/start')) 
async def handler(event):
    await client.send_message(event.chat_id, "Hi there! I'm a bot that can send videos from a specific channel. Use the /getvideo command to get the next video.")

@client.on(events.NewMessage(pattern='/getvideo'))
async def handler(event):
    chat_id = event.chat_id
    target_channel_url = "https://t.me/wifisjcj227"

    await send_next_video(chat_id, target_channel)

async def send_next_video(chat_id, target_channel):
    if chat_id not in latest_video_index:
        latest_video_index[chat_id] = 0  # Initialize index

  async for message in client.iter_messages(target_channel, reverse=True):   # Iterate in reverse
        if message.media and message.media.document:
            if latest_video_index[chat_id] == 0:  # Skip videos already sent
                latest_video_index[chat_id] += 1 
                continue

            try:
                await client.forward_messages(chat_id, message)
                latest_video_index[chat_id] += 1  # Increment for the next video
                return  # Stop iteration once a video is sent
            except Exception as e:
                await client.send_message(chat_id, f"Error forwarding video: {e}")
                return

    # If we reach here, no more videos were found
    await client.send_message(chat_id, "No more videos found in this channel.") 

client.run_until_disconnected()
