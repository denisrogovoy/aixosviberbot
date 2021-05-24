import requests
import json
import buttons
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
from viberbot.api.messages.sticker_message import StickerMessage
from viberbot.api.messages.picture_message import PictureMessage
import time
from datetime import datetime



url="https://api.spacexdata.com/v4/launches/latest"
def main(viber, id):
    switchTrue2 = True
    while True:
        response = json.loads(requests.get(url).content)
        description=response["details"]
        picture=response["links"]["patch"]["small"]
        launch_time=int(response["static_fire_date_unix"])
        print("launch date: ", datetime.utcfromtimestamp(launch_time).strftime('%Y-%m-%d %H:%M:%S'))
        current_time = int(time.time())
        print("current date: ", datetime.utcfromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S'))
        if launch_time<=current_time and switchTrue2==True: #and launch_time+14400>=current_time and switchTrue:
            switchTrue2=False
            print(response)
            print(description)
            pictureSpacex = PictureMessage(media=picture)
            viber.send_messages(id, [TextMessage(text="Ілон Маск сьогодні запустив ракету (rocket), а що за сьогодні зробив корисного ти? (what)"),
                                 pictureSpacex])
            viber.send_messages(id, [TextMessage(text=description), KeyboardMessage(keyboard=buttons.main_keyboard)])
        time.sleep(60)