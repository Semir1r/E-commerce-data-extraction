import nest_asyncio
import os
import csv
import re
import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Load environment variables from .env file
load_dotenv(r'C:\Users\Administrator\Desktop\E-commerce-data-extraction\.env')
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')

# Initialize the Telegram client
client = TelegramClient('scraping_session', api_id, api_hash)

# Define the CSV file to store the data
csv_file = 'telegram_data.csv'

# Function to write messages to the CSV file
def write_to_csv(message_date, sender_id, message_id, amharic_text):
    """Append a message to the CSV file."""
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            message_date, 
            sender_id,
            message_id,
            amharic_text.strip()
        ])

# Function to scrape messages from Telegram channels
async def scrape_telegram_channels(channels):
    """
    Scrapes historical messages from multiple Telegram channels and saves the data to a CSV file.
    Args:
    channels : A list of Telegram channel usernames to scrape.
    """
    await client.start()
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Message Date', 'Sender ID', 'Message ID', 'Product Description'])  # Write CSV header

    for channel_username in channels:
        entity = await client.get_entity(channel_username)
        channel_title = entity.title
        print(f"Scraping historical data from {channel_username} ({channel_title})...")

        async for message in client.iter_messages(entity, limit=300):
            if message.message:
                amharic_reg = r'[\u1200-\u137F0-9\+\-_]+'
                amharic_text = ' '.join(re.findall(amharic_reg, message.message))

                if amharic_text.strip():  # Only write rows with Amharic content
                    message_date = message.date.strftime('%Y-%m-%d %H:%M:%S') if message.date else '[No Date]'
                    sender_id = message.sender_id if message.sender_id else '[No Sender ID]'
                    write_to_csv(message_date, sender_id, message.id, amharic_text)
    
        print(f"Finished scraping {channel_username}")
    print("Historical scraping completed. Listening for real-time messages...")

# Real-time message handler to update the CSV file when new messages arrive
@client.on(events.NewMessage(chats=None))  # Listen to all channels
async def real_time_message_handler(event):
    message = event.message.message
    if message:
        amharic_reg = r'[\u1200-\u137F0-9\+\-_]+'
        amharic_text = ' '.join(re.findall(amharic_reg, message))

        if amharic_text.strip():
            message_date = event.message.date.strftime('%Y-%m-%d %H:%M:%S')
            sender_id = event.message.sender_id if event.message.sender_id else '[No Sender ID]'
            write_to_csv(message_date, sender_id, event.message.id, amharic_text)
            print(f"New message added to CSV: {amharic_text}")

# Wrapper function to start both scraping and real-time updates
def start_scraping(channels):
    """
    Wrapper function to start historical scraping and enable real-time message listening.
    Args:
    channels : A list of Telegram channel usernames to scrape.
    """
    asyncio.run(scrape_telegram_channels(channels))
    client.run_until_disconnected()
