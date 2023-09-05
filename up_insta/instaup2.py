import os
import time
from instabot import Bot

# Initialize an Instagram bot
bot = Bot()
bot.login(username="A.Gatteoo", password="CoolDudes@1")

print("Done")

# Define the directory where your reels are stored
reels_directory = "youtube/data/"

print("Done")

# Define the path to the exist.txt file
exist_txt_path = "exist.txt"

print("Done")

bot.upload_photo("demo.png","Done it 👍")

# # Logout when done
# bot.logout()