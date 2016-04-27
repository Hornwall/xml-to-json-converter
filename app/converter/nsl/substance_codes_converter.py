from lxml import objectify, etree
from operator import itemgetter
from ..xml_converter import XmlConverter
from .substance_code_system_converter import SubstanceCodeSystemConverter

class SubstanceCodeConverter(XmlConverter):
    def convert(self, xml):
        codes = []
        for code in xml.iterchildren():
            item  = {}
            item["code"] = str(code["code"])
            item["code_system_cv"] = SubstanceCodeSystemConverter().convert(code["code-system-cv"])
            codes.append(item)
        return sorted(codes, key = itemgetter("code", "code_system_cv"))
