import moodle, buttons, server, db2_database
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
from queue import Queue

def main(viber, viber_request, condition):
    #global wparData
    #global senderId
    if condition=="Мої оцінки":
        grades = moodle.get_grades(3)
        viber.send_messages(viber_request.sender.id, [TextMessage(text=grades), KeyboardMessage(keyboard=buttons.student_account)])
    elif condition=="Про курс":
        course_name, summary = moodle.get_course_info()
        viber.send_messages(viber_request.sender.id, [TextMessage(text="Назва курсу: {0}\n\nПро курс: {1}".format(course_name, summary)),
                                                      KeyboardMessage(keyboard=buttons.student_account)])
    elif condition=="До головного меню":
        #keyboard = KeyboardMessage(tracking_data='tracking_data', keyboard=buttons.main_menu())
        viber.send_messages(viber_request.sender.id, [TextMessage(text="Чим я можу тобі допомогти? (eyes)"),
                                                      KeyboardMessage(keyboard=buttons.main_keyboard)])
    elif condition=="Запустити WPAR":

        #thread.set_senderId(viber_request.sender.id)
        #print("Запуск", variables.senderId)
        #thread.set_wparData("wpar10 start")
        #print(thread.show_wparData())
        #db2_database.change_wpar_state("wpar 10", viber_request.sender.id, "start")
        wparname = db2_database.get_wpar_name(viber_request.sender.id)
        server.wparQueue.put({"wparname": wparname, "action":"start", "user_id":viber_request.sender.id})
        #server.senderId.put(viber_request.sender.id)
        viber.send_messages(viber_request.sender.id, [TextMessage(text="WPAR запускається (run) \nЗачекайте пару хвилин (zzz)"),
                             KeyboardMessage(keyboard=buttons.student_account)])
        #variables.senderId = viber_request.sender.id
        #variables.wparData ="wpar10 start"
        #print(variables.wparData)
    elif condition=="Зупинити WPAR":
        #db2_database.change_wpar_state("wpar 10", viber_request.sender.id, "stop")
        #server.wparData.put("wpar1 stop")
        #server.senderId.put(viber_request.sender.id)
        wparname=db2_database.get_wpar_name(viber_request.sender.id)
        server.wparQueue.put({"wparname": wparname, "action": "stop", "user_id": viber_request.sender.id})
        viber.send_messages(viber_request.sender.id, [TextMessage(text="WPAR зупиняється (run) \nЗачекайте пару хвилин (zzz)"),
                                                      KeyboardMessage(keyboard=buttons.student_account)])
        #thread.set_senderId(viber_request.sender.id)
        #thread.set_wparData("wpar10 stop")
        #print(thread.show_wparData())
        #variables.senderId= viber_request.sender.id
        #variables.wparData = "wpar10 stop"
        #print(variables.wparData)

