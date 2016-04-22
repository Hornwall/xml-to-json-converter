from lxml import objectify, etree
from operator import itemgetter
from ..xml_converter import XmlConverter

class SubstanceCodeConverter(XmlConverter):
    def convert(self, xml):
        codes = []
        for code in xml.iterchildren():
            item  = {}
            item["code"] = str(code["code"])
            item["code_system"] = str(code["code-system-cv"].attrib["term-id"])
            codes.append(item)
        return sorted(codes, key = itemgetter("code", "code_system"))
