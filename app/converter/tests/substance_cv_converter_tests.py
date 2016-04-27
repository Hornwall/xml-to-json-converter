from .converter_test_case import ConverterTestCase
import os
from ..nsl.substance_cv_converter import SubstanceCVConverter
from lxml import objectify, etree

class SubstanceCVConverterTests(ConverterTestCase):

    def test_substance_code_system_is_expected_to_term_english_equiv(self):
        substance_code_system = SubstanceCVConverter().convert(self.get_substance_codes_system_xml_object())
        self.assertTrue("term_english_equiv" in substance_code_system)

    def test_substance_code_system_is_expected_to_term_english_equiv(self):
        substance_code_system = SubstanceCVConverter().convert(self.get_substance_codes_system_xml_object())
        self.assertTrue("term_id" in substance_code_system)

    def test_substance_code_system_is_expected_to_term_english_equiv(self):
        substance_code_system = SubstanceCVConverter().convert(self.get_substance_codes_system_xml_object())
        self.assertTrue("term_lang" in substance_code_system)

    def test_substance_code_system_is_expected_to_term_english_equiv(self):
        substance_code_system = SubstanceCVConverter().convert(self.get_substance_codes_system_xml_object())
        self.assertTrue("term_revision_num" in substance_code_system)

    def get_substance_codes_system_xml_object(self):
        return self.nsl_xml_obj.substance.common["substance-codes"]["substance-code"][0]["code-system-cv"]
