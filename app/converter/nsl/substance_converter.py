from lxml import objectify, etree
from ..xml_converter import XmlConverter
from .substance_name_converter import SubstanceNameConverter
from .substance_codes_converter import SubstanceCodeConverter

class SubstanceConverter(XmlConverter):
    def convert(self, xml):
        substance = {}
        substance["substance_names"] = SubstanceNameConverter().convert(xml.common["substance-names"])
        substance["substance_codes"] = SubstanceCodeConverter().convert(xml.common["substance-codes"])
        substance["version"] = self.convert_to_iso_date(str(xml.common.versions.version["effective-date"]))
        return substance
