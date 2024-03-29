FROM python:3.9-slim # Or a suitable Python version of your choice

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

COPY . .  # Copy your code files (bot.py, config.py)

CMD ["python", "bot.py"] 
