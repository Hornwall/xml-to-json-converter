from .converter_test_case import ConverterTestCase
import os
from ..nsl.substance_codes_converter import SubstanceCodeConverter
from lxml import objectify, etree

class SubstanceCodesConverterTests(ConverterTestCase):

    def test_substance_code_is_expected_to_have_code(self):
        substance_codes = SubstanceCodeConverter().convert(self.get_substance_codes_xml_object())
        self.assertTrue("code" in substance_codes[0])

    def test_substance_name_is_expected_to_have_type_cv(self):
        substance_codes = SubstanceCodeConverter().convert(self.get_substance_codes_xml_object())
        self.assertTrue("system_cv" in substance_codes[0])

    def test_substance_name_is_expected_to_have_type_cv(self):
        substance_codes = SubstanceCodeConverter().convert(self.get_substance_codes_xml_object())
        self.assertTrue("system_status_cv" in substance_codes[0])

    def test_substance_has_two_names(self):
        substance_codes = SubstanceCodeConverter().convert(self.get_substance_codes_xml_object())
        self.assertEqual(len(substance_codes), 5)

    def get_substance_codes_xml_object(self):
        return self.xml_obj.substance.common["substance-codes"]
