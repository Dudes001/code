import os
import time
from instabot import Bot

# Initialize an Instagram bot
bot = Bot()
bot.login(username="A.Gatteoo", password="CoolDudes@1")

# Define the directory where your reels are stored
reels_directory = "youtube/data/"

# Define the path to the exist.txt file
exist_txt_path = "exist.txt"

# Function to handle rate limiting and retry on 429 error
def upload_with_retry(video_path, caption):
    while True:
        try:
            bot.upload_video(video_path, caption=caption)
            break  # Success, exit the loop
        except Exception as e:
            print(f"Error: {str(e)}")
            if "429" in str(e):
                # If it's a rate-limiting error, wait for a few minutes before retrying
                print("Rate limited. Waiting for 5 minutes...")
                time.sleep(3)  # Wait for 5 minutes before retrying
            else:
                # Handle other exceptions as needed
                break  # Exit the loop on other errors

# Loop through the files in the reels directory
for filename in os.listdir(reels_directory):
    if not filename.endswith(".mp4"):
        continue  # Skip non-video files

    # Check if the file has been uploaded before (in exist.txt)
    with open(exist_txt_path, "r") as exist_file:
        uploaded_reels = exist_file.read().splitlines()
    
    if filename in uploaded_reels:
        continue  # Skip already uploaded reels

    # Upload the reel with rate limit handling
    video_path = os.path.join(reels_directory, filename)
    caption = "Your caption here"
    upload_with_retry(video_path, caption)

    # Append the filename to exist.txt
    with open(exist_txt_path, "a") as exist_file:
        exist_file.write(filename + "\n")

# Logout when done
bot.logout()
