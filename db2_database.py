import ibm_db
import buttons
import time
from ibm_db import connect
from datetime import datetime
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
import secrets

connection = connect(secrets.database +
                     secrets.hostname  + # 127.0.0.1 or localhost works if it's local
                     secrets.port +
                     secrets.protocol +
                     secrets.uid +
                     secrets.ibm_password +
                     'SECURITY=ssl;','','')


def change_wpar_state(wparname, user_id, action):
    sql = "INSERT INTO WPARSSTARTORSTOP (TIME, WPARNAME, USER_ID, ACTION, FINISHED, RESULT, SHOWED) VALUES(?,?,?,?,?,?,?);"
    stmt = ibm_db.prepare(connection, sql)
    time=datetime.now()
    #wparname=wpar
    #action=action
    #finished=False
    #showed=False
    params=[time, wparname, user_id, action, False, None, False]
    for index in range(len(params)):
        print(index+1, params[index])
        ibm_db.bind_param(stmt, index+1, params[index])

    ibm_db.execute(stmt)

def add_user(user_id, user_name, user_avatar, country, language, device_os, api_version, viber_version,
             mobile_country_code, mobil_network_code, device_type):
    sql = "INSERT INTO USERS (SUBSCRIBED_TIME, UNSUBSCRIBED_TIME, USER_ID, USER_NAME, USER_AVATAR, " \
          "COUNTRY, LANGUAGE, DEVICE_OS, API_VERSION, VIBER_VERSION, MOBILE_COUNTRY_CODE, " \
          "MOBILENETWORK_CODE, DEVICE_TYPE) VALUES(?,?,?,?,?,?, ?, ?, ?, ?, ?, ?, ?);"
    stmt = ibm_db.prepare(connection, sql)
    params = [datetime.now(), None, user_id, user_name, user_avatar, country, language, device_os, api_version, viber_version,
             mobile_country_code, mobil_network_code, device_type]
    for index in range(len(params)):
        ibm_db.bind_param(stmt, index+1, params[index])

    ibm_db.execute(stmt)
    # ibm_db.bind_param(stmt, 6, time)
    #ibm_db.execute(stmt)

def delete_user(user_id):
    sql = "SELECT * FROM USERS WHERE USER_ID='"+user_id+"' AND UNSUBSCRIBED_TIME IS NULL;"
    stmt = ibm_db.exec_immediate(connection, sql)
    row = ibm_db.fetch_tuple(stmt)
    print(row)
    if len(row)>0:
        sql = "UPDATE USERS SET UNSUBSCRIBED_TIME='"+str(datetime.now())+"' WHERE ID='" + str(row[0]) + "';"
        stmt = ibm_db.prepare(connection, sql)
        ibm_db.execute(stmt)


def update_user_id(user_id, email):
    sql = "SELECT * FROM WPARS WHERE EMAIL='" + str(email) +"';"
    stmt = ibm_db.exec_immediate(connection, sql)
    row = ibm_db.fetch_tuple(stmt)
    print(row)
    if len(row)>0:
        sql = "UPDATE WPARS SET USER_ID='" + str(user_id)+ "' WHERE ID=" + str(row[0]) + ";"
        stmt = ibm_db.prepare(connection, sql)
        returnCode = ibm_db.execute(stmt)
        print(returnCode)

def get_wpar_name(user_id):
    sql = "SELECT * FROM WPARS WHERE USER_ID='" + str(user_id) + "';"
    stmt = ibm_db.exec_immediate(connection, sql)
    row = ibm_db.fetch_tuple(stmt)
    if len(row)>0:
        return row[1]
    else:
        return None

#def monitoring(viber):
 #   while True:
#        sql = "SELECT * FROM WPARSSTARTORSTOP WHERE FINISHED=1 AND SHOWED=0;"
#        stmt = ibm_db.exec_immediate(connection, sql)
#        row = ibm_db.fetch_tuple(stmt)
#        result = []
 #       while row != False:
 #           print(row)
 #           result += [row]
 #           row = ibm_db.fetch_tuple(stmt)

#        for i in result:
#            sql = "UPDATE WPARSSTARTORSTOP SET SHOWED=1 WHERE ID=" + str(i[0]) + ";"
#            stmt = ibm_db.prepare(connection, sql)
#            returnCode = ibm_db.execute(stmt)
#            viber.send_messages(i[3],
#                                [TextMessage(text="Завдання {0} {1} виконано".format(i[2], i[4])),
#                                 KeyboardMessage(keyboard=buttons.student_account)])
 #           print(returnCode)
#        time.sleep(2)

#def initialize():
#    sql = "INSERT INTO WPARS (WPARNAME, EMAIL) VALUES(?,?);"
#    stmt = ibm_db.prepare(connection, sql)
#    params = [["wpar1", "TomCruise@univ.kiev.ua"], ["wpar2", "SelenaGomez@hollywood.com"], ["wpar3", "RobertPattison@DCcomics.com"],
#              ["wpar4", "OrlandoBloom@hollywood.com"],["wpar5", "GalGabot@DCcomics.com"],["wpar6", "EmmaWatson@WarnerBros.com"],
 #             ["wparTest", "admin@knu.ua"],["wparTeacher", "KonstiantynZarembovskyi@univ.kiev.ua"]]

#    for k in params:
#            ibm_db.bind_param(stmt, 1, k[0])
#            ibm_db.bind_param(stmt, 2, k[1])
#            ibm_db.execute(stmt)

    #ibm_db.execute(stmt)