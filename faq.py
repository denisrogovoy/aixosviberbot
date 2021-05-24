import buttons, texts, dialog
import re
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
from viberbot.api.messages.url_message import URLMessage
from viberbot.api.messages.rich_media_message import RichMediaMessage
from viberbot.api.messages.sticker_message import StickerMessage
from viberbot.api.messages.picture_message import PictureMessage
from random import randint, choice

def faq_options(viber, viber_request, condition):
    print("faq", condition)
    if re.match(r'(?i)(^завдання.*)|(.*(лаб).*(роб).*)', condition):
        viber.send_messages(viber_request.sender.id, [RichMediaMessage(rich_media=buttons.carousel_contentFirstLabs, min_api_version=2, alt_text="Обери потрібну лабораторну роботу"),
                                                      RichMediaMessage(rich_media=buttons.carousel_contentSecondLabs, min_api_version=2, alt_text="Обери потрібну лабораторну роботу"),
                                                      KeyboardMessage(keyboard=buttons.faq_keyboard)])

    elif re.match(r'(?i).*(розклад).*', condition):
        viber.send_messages(viber_request.sender.id, [TextMessage(text=texts.schedule), KeyboardMessage(keyboard=buttons.faq_keyboard)])
    elif re.match(r'(?i).*((вимоги)|(звіт)).*', condition):
        viber.send_messages(viber_request.sender.id, [TextMessage(text=texts.requirements), KeyboardMessage(keyboard=buttons.faq_keyboard)])
    elif re.match(r'(?i)(.*цікав.*факт.*)', condition):
        viber.send_messages(viber_request.sender.id, [TextMessage(text=choice(texts.interesting_facts)), KeyboardMessage(keyboard=buttons.faq_keyboard)])
    elif re.match(r'(?i).*((ssh.*)|(з wpar)).*', condition):
        viber.send_messages(viber_request.sender.id, [TextMessage(text=texts.connect_ssh), URLMessage(media="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html"),
                                                      KeyboardMessage(keyboard=buttons.faq_keyboard)])
    elif condition=="До головного меню":
        #keyboard = KeyboardMessage(tracking_data='tracking_data', keyboard=buttons.main_menu())
        viber.send_messages(viber_request.sender.id, [TextMessage(text="Чим я можу тобі допомогти? (eyes)"),
                                                      KeyboardMessage(keyboard=buttons.main_keyboard)])
    else:
        dialog.main(viber, viber_request, condition)