from .converter_test_case import ConverterTestCase
import os
from ..nsl.substance_converter import SubstanceConverter
from lxml import objectify, etree

class SubstanceConverterTests(ConverterTestCase):

    def test_substance_is_expected_to_have_substance_names(self):
        self.assertTrue("substance_names" in self.get_substance())

    def test_substance_is_expected_to_have_substance_codes(self):
        self.assertTrue("substance_codes" in self.get_substance())
    
    def test_substance_is_expected_to_have_version(self):
        self.assertTrue("version" in self.get_substance())

    def get_substance(self):
        return SubstanceConverter().convert(self.nsl_xml_obj.substance)
