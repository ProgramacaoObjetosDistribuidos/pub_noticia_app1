#!usr/bin/env python
import socket
# from classes import News

__author__ = 'Joao Marcos F'

TCP_IP = '25.13.81.204'
TCP_PORT = 1231
BUFFER_SIZE = 1024

# encodeImg = News.encodeImg("/home/joaomarcos/Pictures/Venda.png")
# noticia = News("joao","noticia","noticia de algo", "Conteudo da noticia", encodeImg, False)

def publish(noticia):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((TCP_IP, TCP_PORT))
    info = conn.recv(BUFFER_SIZE)
    print "Server response:",info

    msg = noticia.toXml()+"\n"

    totalsent = 0
    while totalsent < len(msg):
        sent = conn.send(msg[totalsent:])
        totalsent += sent

    info = conn.recv(BUFFER_SIZE)
    print "Server response: "+info
    conn.close()
# import xml.etree.ElementTree as ET
# xml = ET.parse("ok.xml")
# for child in xml._root:
#     for noticia in child:
#         print noticia.text
