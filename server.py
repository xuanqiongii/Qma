import socket

HOST = '172.29.45.176'
PORT = 65000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

client, address = server.accept()

while True:
    print(f'{address}连接')
    cmd_input = input("输入命令\n")
    client.send(cmd_input.encode('utf-8'))
    print(client.recv(1024).decode('utf-8', errors='ignore'))
