import socket


Head=64
port = 5000
disconnect = "!DISCONNECT"
format = "utf-8"
SERVER =socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,port)

client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(format)
    msg_length=len(message)
    send_length =str(msg_length).encode(format)
    send_length += b' '* (Head -len(send_length))
    client.send(send_length)
    client.send(message)

send("Hii")
send("Hello")
send("How r u")
