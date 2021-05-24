import mail, functions, buttons, texts, moodle
from viberbot.api.messages.keyboard_message import KeyboardMessage
from viberbot.api.messages.text_message import TextMessage

def main(viber, viber_request, userrole, sendMessageToUser, securityCode):
    moodle.verification_to_moodle(sendMessageToUser, userrole)
    if userrole[0]==0:
        choice = False
        #global securityCode
        mail.sendEmail(sendMessageToUser, securityCode[0], choice)
    else:
        choice=True
        securityCode[0]=functions.random_with_N_digits(7)
        mail.sendEmail(sendMessageToUser, securityCode[0], choice)
        viber.send_messages(viber_request.sender.id, [TextMessage(text=texts.mail_validation)])