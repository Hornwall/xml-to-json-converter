from lxml import objectify, etree
from .converter_test_case import ConverterTestCase
from ..nsl.other.recommended_name_converter import RecommendedNameConverter

class RecommendedNameConverterTests(ConverterTestCase):
    def test_recommended_name_is_expected_to_have_name(self):
        self.assertTrue("name" in self.get_name())

    def test_recommended_name_is_expected_to_have_recommended_name_class_lx(self):
        self.assertTrue("recomended_name_class_lx" in self.get_name())

    def get_name(self):
        return RecommendedNameConverter().convert(self.nsl_other_xml_obj["NSL_Substance"]["RecommendedName"])
