# Use the official Python image as base
FROM python:3.9-slim

# Set environment variables
ENV API_ID=YOUR_API_ID \
    API_HASH=YOUR_API_HASH \
    BOT_TOKEN=YOUR_BOT_TOKEN

# Install dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot files
COPY . /app

# Run the bot
CMD ["python", "bot.py"]
