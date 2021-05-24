import buttons, texts, faq, verification, studentAccount, db2_database
import re
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
from viberbot.api.messages.contact_message import ContactMessage
from viberbot.api.messages.sticker_message import StickerMessage
from viberbot.api.messages.picture_message import PictureMessage

email=""

def main_options(viber, viber_request, userrole, securityCode, usermessage):
    keyboard = KeyboardMessage(keyboard=buttons.main_keyboard)
    print("---------------------------------------------------")
    print(viber_request.message)
    global email
    if isinstance(viber_request.message, TextMessage):

        if re.match(r'(?i)(.*(FAQ).*)', usermessage):
            viber.send_messages(viber_request.sender.id, [TextMessage(text="Обери питання, яке тебе цікавить (Q): "),
                                                          KeyboardMessage(keyboard=buttons.faq_keyboard)])
        elif re.match(r'(?i).*(увійти)|(особистий)|(приватний).*кабінет.*', usermessage):
            #viber.send_messages(viber_request.sender.id, [TextMessage(text=texts.sign_in), keyboard])
            if userrole[0] == 0:
                viber.send_messages(viber_request.sender.id, [TextMessage(text=texts.sign_in), KeyboardMessage(keyboard=buttons.share_phone, min_api_version=3)])

            elif userrole[0] == 1:
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Ви увійшли до особистого кабінету студента (nerd)"), KeyboardMessage(keyboard=buttons.student_account)])
            elif userrole[0] == 2:
                viber.send_messages(viber_request.sender.id, [TextMessage(text="Ви увійшли до особистого кабінету викладача (rockon)"), keyboard])
        elif re.match(r'(?i).*((допомога)|(хелп)|(help)|(довідка)).*', usermessage):
            viber.send_messages(viber_request.sender.id, [TextMessage(text=texts.help), keyboard])
        elif re.match(r'(?i).*(зв\'язок)|(написати)|(зв\'язатися).*викладач.*', usermessage):
            viber.send_messages(viber_request.sender.id, [TextMessage(text="Задай питання, яке тебе цікавить викладачу нижче: "), keyboard])
        elif re.match(r'.*@.*', usermessage):

            email=usermessage
            verification.main(viber, viber_request, userrole, usermessage, securityCode)
        elif re.match(r'\d\d\d\d\d\d\d', usermessage):
            #print(condition, "!!!", securityCode, userrole)
            if int(usermessage)==int(securityCode[0]):
                if userrole[0] == 0:
                    viber.send_messages(viber_request.sender.id, [TextMessage(text=texts.error_registration)])
                elif userrole[0] == 1:
                    viber.send_messages(viber_request.sender.id, [TextMessage(text="Вітаю! (wink) Ви увійшли до особистого кабінету студента (nerd)"), KeyboardMessage(keyboard=buttons.student_account)])

                    db2_database.update_user_id(viber_request.sender.id, email)
                elif userrole[0] == 2:
                    viber.send_messages(viber_request.sender.id, [TextMessage(text="Вітаю! (wink) Ви увійшли до особистого кабінету викладача (rockon)"), keyboard])
        elif userrole[0]==1:
            studentAccount.main(viber, viber_request, usermessage)
        else:
            faq.faq_options(viber, viber_request, usermessage)
    elif isinstance(viber_request.message, ContactMessage):
        #viber.send_messages(viber_request.sender.id, [TextMessage(text=viber_request.message.contact.phone_number), keyboard])
        #print(viber_request.message.contact)
        viber.send_messages(viber_request.sender.id, [TextMessage(text="Введіть свій e-mail для перевірки нижче (letter): ")])
    #elif isinstance(viber_request.message, StickerMessage):
      #  print("Sticker")
      #  print(viber_request.message)
       # viber.send_messages(viber_request.sender.id, [TextMessage(text=viber_request.message.sticker_id)])

