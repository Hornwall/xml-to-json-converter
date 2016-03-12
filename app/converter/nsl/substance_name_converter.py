from lxml import objectify, etree
from ..xml_converter import XmlConverter

class SubstanceNameConverter(XmlConverter):
    def convert(self, xml):
        names = []
        for name in xml.iterchildren():
            item = {}
            item["name"] = name["substance-name"].text
            item["type_cv"] = name["substance-name-type-cv"].text
            item["language_cv"] = name["language-cv"].text
            names.append(item)
        return names
