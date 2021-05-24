from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
import logging
import re
from logdna import LogDNAHandler
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
from viberbot.api.messages.sticker_message import StickerMessage
from viberbot.api.messages.picture_message import PictureMessage
from threading import Thread

import buttons, texts, main_menu, db2_database, server, spacex, ibm_translator, secrets
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest
import secrets

bot_configuration = BotConfiguration(
	name='AIX Bot',
	avatar='https://aixbot.s3.amazonaws.com/avatarmin.png',
	auth_token=secrets.viber_auth_token

)
viber = Api(bot_configuration)

from flask import Flask, request, Response

#apiKey = '6161d5eed2ebb9cdc8add24e6e9b0c98'
apiKey = secrets.logdna_api_key
logger = logging.getLogger('logdna')
logger.setLevel(logging.INFO)

options = {
  'hostname': 'aixbot.pp.ua',
  'ip': '100.25.183.46',
  'mac': '06:e6:89:04:7f:97'
  #'url':'https://logs.eu-gb.logging.cloud.ibm.com/logs/ingest'
}
options['index_meta'] = True

handler = LogDNAHandler(apiKey, options)
logger.addHandler(handler)
#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)
#handler = logging.StreamHandler()
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)
#logger.addHandler(handler)

app = Flask(__name__)

userrole = [0] #0 - guest, 1 - student, 2 - teacher
securityCode=[0]
from queue import Queue


rootId="x9sFVcYKD2F74K+E1ruH7w=="
#thread = Thread(target=db2_database.monitoring, args=(viber,))
threadServer = Thread(target=server.listen, args=(viber,))
threadSpacex = Thread(target=spacex.main, args=(viber,rootId,))
switch=True
switchTrue=True

@app.route('/', methods=['POST'])
def incoming():
    try:
        global switch

        if switch:
            switch = False
            threadServer.start()

        global switchTrue
        if switchTrue:
            switchTrue=False
            threadSpacex.start()
        logger.info("received request. post data: {0}".format(request.get_data()))
        # every viber message is signed, you can verify the signature using this method
        if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
            logger.error("Signature not valid. Response code 403.")
            return Response(status=403)

        # this library supplies a simple way to receive a request object
        viber_request = viber.parse_request(request.get_data())

        if isinstance(viber_request, ViberMessageRequest):
            logger.info('Received message from user', {"meta": {"messagetype": "message"}})
            #print(viber_request.message.text)
            #viber.send_messages(viber_request.sender.id, [TextMessage(text=viber_request.message.text),
             #                                           KeyboardMessage(keyboard=buttons.main_keyboard)])
            #print(viber_request.sender.id)
            usermessage=viber_request.message.text
            if not re.match(r'(.*@.*)|(.*\d.*)|(.*FAQ.*)', usermessage):
                usermessage=ibm_translator.translate(viber_request.message.text)
            print(usermessage)
            main_menu.main_options(viber, viber_request, userrole, securityCode, usermessage)
        elif isinstance(viber_request, ViberSubscribedRequest):
            print(viber_request.user.id)

            pictureMinion = PictureMessage(media="https://aixbot.s3.amazonaws.com/stickerWelcome.jpg", text=texts.welcome)
            viber.send_messages(viber_request.user.id, [pictureMinion, TextMessage(text=texts.hint), KeyboardMessage(keyboard=buttons.main_keyboard)])
            #-user_data = Api.get_user_details(viber, viber_request.user.id)
            #-print(user_data)
            #db2_database.add_user(user_data["id"], user_data["name"], user_data["avatar"], user_data["country"], user_data["language"],
            #                    user_data["primary_device_os"], user_data["api_version"], user_data["viber_version"], user_data["mcc"],
            #                  user_data["mnc"], user_data["device_type"])
            logger.info('User {0} subscribed.'.format(viber_request.user.id), {"meta":{"useraction":"subscribed"}})
        elif isinstance(viber_request, ViberConversationStartedRequest):
            #Когда пользователь не подписался еще на чат-бот и просто в первый раз открыл чат-бот (сообщение приветсвие)
            if (viber_request.context=='siri'):
                viber.send_messages(viber_request.user.id, [TextMessage(text=texts.siri_message), KeyboardMessage(keyboard=buttons.main_keyboard)])
            else:
                viber.send_messages(viber_request.user.id, [TextMessage(text=texts.hello_message)])
        elif isinstance(viber_request, ViberUnsubscribedRequest):
            userId=viber_request.user_id
            logger.info('User {0} unsubscribed.'.format(userId), {"meta":{"useraction":"unsubscribed"}})
            #-db2_database.delete_user(userId)
        #    print(viber_request)
        #    print("hellp")
        #    viber.send_messages(viber_request.user_id, [TextMessage(text="Good Bye!")])

        elif isinstance(viber_request, ViberFailedRequest):
            logger.warning("client failed receiving message. failure: {0}".format(viber_request))
        #logger.info("Response code 200")
        return Response(status=200)
    except Exception as e:
        logger.error("Error occured. {0}".format(e))
        print(e)

if __name__ == "__main__":
    #thread = Thread(target=server.listen, args=(viber,))
    #thread.start()
    logger.info('ViberBot is running.')
    #main()
    #botFunction()
    #db2_change_wpar_status.main("wpar1", "start")
    context = ('fullchain.pem', 'privkey.pem')
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)

    #db2.main()