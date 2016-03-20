from lxml import objectify, etree
from ...xml_converter import XmlConverter

class RecommendedNameConverter(XmlConverter):
    def convert(self, xml):
        name = {}
        name["name"] = xml["Name"]
        name["recomended_name_class_lx"] = xml["RecommendedNameClassLx"]
        return name
