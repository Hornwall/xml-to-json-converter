from lxml import objectify, etree
from .converter_test_case import ConverterTestCase
from ..nsl.other.substance_relation_converter import SubstanceRelationConverter

class SubstanceRelationConverterTests(ConverterTestCase):
    def test_relation_is_expected_to_have_related_nsl_id(self):
        self.assertTrue("related_nsl_id" in self.get_relation())

    def test_relation_is_expected_to_have_subst_subst_relation_lx(self):
        self.assertTrue("subst_subst_relation_lx" in self.get_relation())

    def get_relation(self):
        return SubstanceRelationConverter().convert(self.nsl_other_xml_obj["NSL_Substance"]["SubstanceSubstanceRelation"])
