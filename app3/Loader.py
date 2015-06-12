import socket
import xml.etree.ElementTree as ET
from auth import Browser
import gtk
from classes import News

TCP_IP = '192.168.0.169'
TCP_PORT_LOGIN = 1234
TCP_PORT_LISTEN = 1231
BUFFER_SIZE = 1024
TOKEN = ''
# APP = DesktopApp()

def send_msg(channel, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = channel.send(msg[totalsent:])
        totalsent += sent
"""
def notify(news):

    for news.len
"""
class Response:
    def __init__(self):
        self.error = ''

    def fromXml(self, xml):
        root = ET.fromstring(xml)
        for child in root:
            if child.tag == 'session':
                self.session = child.text
            elif child.tag == 'name':
                self.name = child.text
            elif child.tag == 'email':
                self.email = child.text
            elif child.tag == 'error':
                self.error = child.text

def connect(token):
    try:

        channel_login = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        channel_login.connect((TCP_IP, TCP_PORT_LOGIN))

        send_msg(channel_login, token)

        print token

        info = channel_login.recv(1024)
        print info
        response = Response()
        response.fromXml(info)
        channel_login.close()

        print response.error

        if response.error == '':
            channel_news = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            channel_news.connect((TCP_IP, TCP_PORT_LISTEN))
            print "waiting for news"
            msg = "HASNOTIFICATION:"+response.session+"\n"

            send_msg(channel_news, msg)
            # open thread for notificator
            # take a reference for it
            connected = True
            while connected:
                print "A receber.."
                info = channel_news.recv(BUFFER_SIZE)
                print info
                if info == None or info == '':
                    connected = False
    except KeyboardInterrupt or SystemExit or Exception:
        channel_news.close()
        print "fechou a caceta!"
                #send a message for a notificator with the new notices


def get_token():
    with open("access_token.txt","rb") as token_file:
        token = token_file.read()
    return token

if (__name__ == '__main__'):
    # Creates the browser
    # app.start()
    token = get_token()
    connect("TOKEN:"+get_token()+"\n")

    print "finish"