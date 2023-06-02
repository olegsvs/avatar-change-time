"""
Сделано на основе поста https://habr.com/ru/post/457078/ (@mumtozvalijonov)

с моими небольшими доработками
"""
from telethon import TelegramClient, sync
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
import time
from datetime import datetime, timedelta
from config import *
from generate_time_images import *
import logging
import os

# Enable logging
logging.basicConfig(
    filename=datetime.now().strftime('logs/log_%d_%m_%Y_%H_%M.log'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

client = TelegramClient('my_session9911', api_id, api_hash)
client.start()

#curr_time_text="00:00"
start_time = datetime.utcnow()
start_text = convert_time_to_string(start_time)
while True:
    curr_time = datetime.utcnow()
    curr_text = convert_time_to_string(curr_time)
    if curr_text != start_text:
        start_text=curr_text
        change_img()
        file = client.upload_file(f"time.png")
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        client(UploadProfilePhotoRequest(file))
        logger.info("Update time")
    logger.info("Tick")
    time.sleep(1)

if __name__ == '__main__':
	pass
