import socket
import time
from threading import Thread

data="none"
sock = socket.socket()
sock.connect(('100.25.183.46', 9090))

def connect(sock):
    while True:
        try:
            global data
            if data!="none":
                sock.send((data+"was started").encode())
                data="none"
            data = sock.recv(1024).decode()
            print(data)
            time.sleep(2)
        except:
            sock.close()

thrd = Thread(target=connect, args=(sock,))
thrd.start()