from lxml import objectify, etree
from ...xml_converter import XmlConverter
from .substance_other_converter import SubstanceOtherConverter

class NslOtherConverter(XmlConverter):
    def convert(self, xml):
        substances = []
        for substance in xml.iterchildren():
            substances.append(SubstanceOtherConverter().convert(substance))
        return substances
