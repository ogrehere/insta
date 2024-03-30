# Telegram Phone Number Info Bot

![Bot Logo](https://telegra.ph/file/f0b21cd8808d4fc97eb62.png)

This Telegram bot provides information about phone numbers. Users can send a phone number to the bot, and it will reply with information such as the carrier, country, and timezone associated with that number.

## Features

- Retrieves information about phone numbers including carrier, country, and timezone.
- Requires users to join specific Telegram channels before accessing the bot's features.

## Requirements

- Python 3.x
- Pyrogram
- phonenumbers
- geocoder

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/telegram-phone-info-bot.git
   cd telegram-phone-info-bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain Telegram API credentials and bot token.

4. Update the `API_ID`, `API_HASH`, and `BOT_TOKEN` variables in the `bot.py` file with your actual credentials.

5. Customize the `REQUIRED_CHANNELS` list in the `bot.py` file with the channels you want users to join before accessing the bot.

6. Run the bot:

   ```bash
   python bot.py
   ```

## Usage

1. Start the bot by sending the `/start` command.
2. Follow the instructions to join the required channels if you haven't already.
3. Send a phone number to the bot to receive information about it.

## Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your_feature_name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your_feature_name`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
`