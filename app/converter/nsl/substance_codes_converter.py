from lxml import objectify, etree
from ..xml_converter import XmlConverter

class SubstanceCodeConverter(XmlConverter):
    def convert(self, xml):
        codes = []
        for code in xml.iterchildren():
            item  = {}
            item["code"] = str(code["code"])
            item["system_cv"] = str(code["code-system-cv"])
            item["system_status_cv"] = str(code["code-system-status-cv"])
            codes.append(item)
        return codes
