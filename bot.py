import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import instaloader
from config import TELEGRAM_BOT_TOKEN, CHANNEL_ID

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to Instagram Video Downloader Bot! Send me the Instagram post URL and I will download the video for you.')

# Function to handle the message containing Instagram URL
def download_instagram_video(update: Update, context: CallbackContext) -> None:
    # Extract the Instagram URL from the message
    url = update.message.text
    
    # Check if the user is a member of the channel
    if not context.bot.get_chat_member(CHANNEL_ID, update.message.from_user.id).status == 'member':
        update.message.reply_text("Please join the channel to use this bot.")
        return

    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Download the video
        post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])
        loader.download_post(post, target='.')
        
        # Get the downloaded video file
        video_filename = f"{post.owner_username}_{post.date_utc.strftime('%Y%m%d')}.mp4"
        
        # Send the video file to the user
        update.message.reply_video(video=open(video_filename, 'rb'))
        
        # Delete the downloaded video file
        os.remove(video_filename)
    
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Register message handler for Instagram URLs
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, download_instagram_video))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()

