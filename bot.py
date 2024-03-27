from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup

# Function to scrape video links from the channel
def scrape_videos(channel_url):
    response = requests.get(channel_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    video_tags = soup.find_all('a', class_='video-link')  # Adjust class name as per your channel's HTML structure
    video_urls = [tag['href'] for tag in video_tags]
    return video_urls

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Hexor bot! Click the Hexor button to get a video from the channel.")

# Function to handle button clicks
def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == 'hexor':
        channel_url = 'https://t.me/+YokGKELJu9YwZDk1'  # Replace with your channel URL
        video_urls = scrape_videos(channel_url)
        
        click_count = context.user_data.get('click_count', 0)
        if click_count < len(video_urls):
            query.message.reply_video(video_urls[click_count])
            context.user_data['click_count'] = click_count + 1
        else:
            query.message.reply_text("No more videos available.")

# Main function to start the bot
def main() -> None:
    updater = Updater("6707583022:AAEahTtTAlqL0ujzwbkNNSLGorFlBs63CRQ")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_click))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
