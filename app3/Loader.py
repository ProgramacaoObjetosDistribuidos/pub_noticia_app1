__author__ = 'joaomarcos'
import xml.etree.ElementTree as ET

class Response:

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

if (__name__ == '__main__'):
    with open('response.xml', 'rb') as xml_file:
        xml = xml_file.read()
        response = Response()
        response.fromXml(xml)

        print response.name

