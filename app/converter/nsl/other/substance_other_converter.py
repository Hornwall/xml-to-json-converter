from lxml import objectify, etree
from ...xml_converter import XmlConverter
from .recommended_name_converter import RecommendedNameConverter
from .substance_relation_converter import SubstanceRelationConverter

class SubstanceOtherConverter(XmlConverter):
    def convert(self, xml):
        substance = {}
        substance["se_nsl_id"] = xml["SeNSLid"]
        if hasattr(xml, "NarcoticClass"):
            substance["narcotic_class"] = xml["NarcoticClass"]
        else:
            substance["narcotic_class"] = None

        substance["recomended_name"] = RecommendedNameConverter().convert(xml["RecommendedName"])

        if hasattr(xml, "SubstanceSubstanceRelation"):
            relations = []
            for relation in xml.iterchildren():
                if hasattr(relation, "RelatedSeNSLid"):
                    relations.append(SubstanceRelationConverter().convert(relation))
            substance["substance_substance_relations"] = relations
        else:
            substance["substance_substance_relations"] = []

        return substance
