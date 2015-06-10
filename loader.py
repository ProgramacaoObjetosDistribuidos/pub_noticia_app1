#!usr/bin/env python
import socket
# from classes import News

__author__ = 'Joao Marcos F'

TCP_IP = '10.42.0.1'
TCP_PORT = 12345
BUFFER_SIZE = 1024

# encodeImg = News.encodeImg("/home/joaomarcos/Pictures/Venda.png")
# noticia = News("joao","noticia","noticia de algo", "Conteudo da noticia", encodeImg, False)

def publish(noticia):
    # conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # conn.connect((TCP_IP, TCP_PORT))
    # info = conn.recv(BUFFER_SIZE)
    # print "Server response:",info

    msg = noticia.toXml()+"\n"
    print msg
    # totalsent = 0
    # while totalsent < len(msg):
    #     sent = conn.send(msg[totalsent:])
    #     totalsent += sent
    #
    # info = conn.recv(BUFFER_SIZE)
    # print "Server response: "+info
    # conn.close()
