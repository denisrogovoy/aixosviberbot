import time
import buttons
from queue import Queue
import json
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage

import socket

wparQueue=Queue()


def listen(viber):

    sock = socket.socket()
    sock.bind(('172.31.53.92', 9090))
    sock.listen(1)
    conn, addr = sock.accept()

    print('connected:', addr)
    try:
        while True:
            data = conn.recv(1024).decode()
            jsonData=json.loads(data)
            print(jsonData)
            if jsonData['wparname']!='none':
                print("trueeee")
                #+str(jsonData['action'])
                if jsonData['action']=='start':
                    viber.send_messages(jsonData['user_id'], [TextMessage(text=str(jsonData['wparname'])+" успішно запущено (checkmark)"),
                                                          KeyboardMessage(keyboard=buttons.student_account)])
                elif jsonData['action']=='stop':
                    viber.send_messages(jsonData['user_id'],
                                    [TextMessage(text=str(jsonData['wparname']) + " успішно зупинено (checkmark)"),
                                     KeyboardMessage(keyboard=buttons.student_account)])
            #global wparData
            #if wparData!="none":
            #print(wparQueue.qsize())
            if wparQueue.qsize()>0:
                wparEntity = wparQueue.get()
                print(wparEntity["wparname"])
                sendingData = {'wparname': wparEntity['wparname'], 'action':wparEntity['action'], 'user_id':wparEntity['user_id']}
                conn.send(json.dumps(sendingData).encode())
            else:
                sendingData = {'wparname':'none', 'action':'none', 'user_id':'none'}
                conn.send(json.dumps(sendingData).encode())
            #print(wparData)
            #if wparData.qsize() == 0:
            #    wparData.put("none")
            #    print("none")
            #print(wparData)
            time.sleep(2)
    except Exception as e:
        conn.close()
        print("Server error:", e)