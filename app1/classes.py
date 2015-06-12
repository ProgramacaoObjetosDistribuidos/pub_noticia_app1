__author__ = 'joaomarcos'
import base64

import xml.etree.ElementTree as ET

class News:
    def __init__(self, publishers, title, summary, content, encodingImg, status):
        self.publishers = publishers
        self.title = title
        self.summary = summary
        self.content = content
        self.image = encodingImg
        self.status = status

    @classmethod
    def encodeImg(self, imgPath):
        with open(imgPath, "rb") as imageFile:
            string = base64.b64encode(imageFile.read())
        return string

    def decodeImg(self, strCode):
        return base64.decodestring(strCode)

    def toXml(self):
        News = ET.Element('noticia')
        child_aut = ET.SubElement(News, 'autor')
        child_aut.text = self.publishers
        child_title = ET.SubElement(News, 'titulo')
        child_title.text = self.title
        child_summary = ET.SubElement(News, 'resumo')
        child_summary.text = self.summary
        child_content = ET.SubElement(News, 'conteudo')
        child_content.text = self.content
        child_img = ET.SubElement(News, 'imagem')
        child_img.text = self.image
        child_stt = ET.SubElement(News, 'lida')
        child_stt.text = self.status
        ET.dump(News)
        return ET.tostring(News)

    @classmethod
    def newsFromXml(self, xml):
        etNews = ET.fromstring(xml)
        for child in etNews:
            if child.tag == 'autor':
                pubhiser = child.text
            if child.tag == 'titulo':
                title = child.text
            if child.tag == 'resumo':
                summary = child.text
            if child.tag == 'conteudo':
                content = child.text
            if child.tag == 'imagem':
                image = child.text
            if child.tag == 'lida':
                status = child.text
        news = self(pubhiser, title, summary, content, image, status)
        return news