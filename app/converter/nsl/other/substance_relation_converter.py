from lxml import objectify, etree
from ...xml_converter import XmlConverter

class SubstanceRelationConverter(XmlConverter):
    def convert(self, xml):
        relation = {}
        relation["related_nsl_id"] = xml["RelatedSeNSLid"]
        relation["subst_subst_relation_lx"] = xml["SubstSubstRelationLx"]
        return relation
