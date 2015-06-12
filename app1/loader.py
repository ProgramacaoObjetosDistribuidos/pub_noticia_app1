#!usr/bin/env python
import socket
# from classes import News
from threading import Thread

__author__ = 'Joao Marcos F'

TCP_IP = '10.10.2.39'
TCP_PORT = 1231
BUFFER_SIZE = 1024

# encodeImg = News.encodeImg("/home/joaomarcos/Pictures/Venda.png")
# noticia = News("joao","noticia","noticia de algo", "Conteudo da noticia", encodeImg, False)
class Publisher(Thread):

    def __init__(self):
        Thread.__init__(self)

    def set_news(self, news):
        self.news = news

    def log(self, info):
        with open("log.txt","ab") as log:
            log.write("Server response: "+info)

    def publish(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((TCP_IP, TCP_PORT))
        info = conn.recv(BUFFER_SIZE)

        self.log(info)

        msg = self.news.toXml()+"\n"

        totalsent = 0
        while totalsent < len(msg):
            sent = conn.send(msg[totalsent:])
            totalsent += sent

        info = conn.recv(BUFFER_SIZE)

        self.log(info)

        conn.close()

    def run(self):
        self.publish()
# import xml.etree.ElementTree as ET
# xml = ET.parse("ok.xml")
# for child in xml._root:
#     for news in child:
#         print news.text
