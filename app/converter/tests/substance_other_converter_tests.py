from lxml import objectify, etree
from .converter_test_case import ConverterTestCase
from ..nsl.other.substance_other_converter import SubstanceOtherConverter


class SubstanceOtherConverterTests(ConverterTestCase):
    def test_substance_is_expected_to_have_se_nsl_id(self):
        self.assertTrue("se_nsl_id" in self.get_substance())

    def test_substance_is_expected_to_have_narcotic_class(self):
        self.assertTrue("narcotic_class" in self.get_substance())

    def test_substance_is_expected_to_have_narcotic_class(self):
        self.assertTrue("recomended_name" in self.get_substance())

    def test_substance_is_expected_to_have_narcotic_class(self):
        self.assertTrue("substance_substance_relations" in self.get_substance())

    def test_substance_is_expected_to_have_two_relations(self):
        self.assertEqual(len(self.get_substance()["substance_substance_relations"]), 2)

    def get_substance(self):
        return SubstanceOtherConverter().convert(self.nsl_other_xml_obj["NSL_Substance"])
