import xml.etree.ElementTree as ET
import os


class XML_Lib:
    def reader(self, key, innerRoot):
        try:
            dir_name = os.path.dirname(__file__)
            path = os.path.join(dir_name, 'data.xml')
            source = open(path, 'rb')
            xml_path = ET.parse(source, None)
            root = xml_path.getroot()
            for x in root.findall(innerRoot):
                value = x.find(key).text
            return value
        except NameError:
            print('An Exception occurred in reader method')















