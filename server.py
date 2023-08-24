import socket
import threading
import time

Head=64
port = 5000
disconnect = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname()) #TO get the localhost ip address
format = "utf-8"

acces = (SERVER,port)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#AF_INET is a ipv4 address and sock_stream to get the stream of data sharing

server.bind(acces)


def client(conn,addr):
    print(f"[NEW CONNECTION ]{addr} connected")
    connection=True
    while connection:
        msg_len = conn.recv(Head).decode(format)
        if msg_len:
            msg_len = int(msg_len)
            msg=conn.recv(msg_len).decode(format)
            print(f"[{addr}] {msg}")
            if msg == disconnect:
                connection = False
            print(f"[{addr}] {msg}")
    conn.close()



def start():
    server.listen()
    print(f"the ip address listen is {SERVER}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=client,args=(conn,addr))
        thread.start()
        print(f'active connection{threading.active_count()-1}')

print("the server is starting")
start()
