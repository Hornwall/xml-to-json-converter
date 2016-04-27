from lxml import objectify, etree
from operator import itemgetter
from ..xml_converter import XmlConverter

class SubstanceCVConverter(XmlConverter):
    def convert(self, xml):
        item  = {}
        item["term_english_equiv"] = str(xml.attrib["term-english-equiv"])
        item["term_id"] = str(xml.attrib["term-id"])
        item["term_lang"] = str(xml.attrib["term-lang"])
        item["term_revision_num"] = str(xml.attrib["term-revision-num"])
        return item
