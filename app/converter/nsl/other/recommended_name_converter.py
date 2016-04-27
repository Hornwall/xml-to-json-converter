from lxml import objectify, etree
from ...xml_converter import XmlConverter

class RecommendedNameConverter(XmlConverter):
    def convert(self, xml):
        name = {}
        name["name"] = str(xml["Name"])
        name["recommended_name_class_lx"] = str(xml["RecommendedNameClassLx"])
        return name
