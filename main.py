import time

from telethon import TelegramClient

from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest

from config import api_hash, api_id
from utils import time_has_changed, generate_time_image_bytes
from datetime import datetime, timedelta


client = TelegramClient("carpediem", api_id, api_hash)
client.start()


async def main():
    prev_update_time = datetime.now() - timedelta(minutes=1)

    while True:
        if time_has_changed(prev_update_time):
            bts = generate_time_image_bytes(datetime.now())
            await client(DeletePhotosRequest(await client.get_profile_photos('me')))
            file = await client.upload_file(bts)
            await client(UploadProfilePhotoRequest(file))
            prev_update_time = datetime.now()
            time.sleep(1)
            

if __name__ == '__main__':
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
