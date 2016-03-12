from lxml import objectify, etree
from ..xml_converter import XmlConverter
from .substance_converter import SubstanceConverter

class NslConverter(XmlConverter):
    def convert(self, xml):
        substances = []
        for substance in xml.substance.iterchildren():
            substances.append(SubstanceConverter().convert(substance))
        return substances
