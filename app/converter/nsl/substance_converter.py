from lxml import objectify, etree
from ..xml_converter import XmlConverter
from .substance_name_converter import SubstanceNameConverter
from .substance_codes_converter import SubstanceCodeConverter

class SubstanceConverter(XmlConverter):
    def convert(self, xml):
        substance = {}
        substance["substance_names"] = SubstanceNameConverter().convert(xml["substance-names"])
        substance["substance_codes"] = SubstanceCodeConverter().convert(xml["substance-codes"])
        return substance
