from lxml import objectify, etree
from ..xml_converter import XmlConverter

class SubstanceCodeConverter(XmlConverter):
    def convert(self, xml):
        codes = []
        for code in xml.iterchildren():
            item  = {}
            item["code"] = code["code"]
            item["system_cv"] = code["code-system-cv"]
            item["system_status_cv"] = code["code-system-status-cv"]
            codes.append(item)
        return codes
