from lxml import objectify, etree
from operator import itemgetter
from ..xml_converter import XmlConverter
from .substance_cv_converter import SubstanceCVConverter

class SubstanceCodeConverter(XmlConverter):
    def convert(self, xml):
        codes = []
        for code in xml.iterchildren():
            item  = {}
            item["code"] = str(code["code"])
            item["code_system_cv"] = SubstanceCVConverter().convert(code["code-system-cv"])
            item["code_system_status_cv"] = SubstanceCVConverter().convert(code["code-system-status-cv"])
            codes.append(item)
        return sorted(codes, key = itemgetter("code"))
