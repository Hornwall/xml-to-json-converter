from lxml import objectify, etree
from operator import itemgetter
from ..xml_converter import XmlConverter

class SubstanceNameConverter(XmlConverter):
    def convert(self, xml):
        names = []
        for name in xml.iterchildren():
            item = {}
            item["name"] = name["substance-name"].text
            item["language_cv"] = name["language-cv"].text
            names.append(item)
        return sorted(names, key = itemgetter("name", "language_cv"))
