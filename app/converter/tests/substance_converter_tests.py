from .converter_test_case import ConverterTestCase
import os
from ..nsl.substance_converter import SubstanceConverter
from lxml import objectify, etree

class SubstanceConverterTests(ConverterTestCase):

    def test_substance_is_expected_to_have_substance_names(self):
        substance = SubstanceConverter().convert(self.xml_obj.substance.common)
        self.assertTrue("substance_names" in substance)

    def test_substance_is_expected_to_have_substance_codes(self):
        substance = SubstanceConverter().convert(self.xml_obj.substance.common)
        self.assertTrue("substance_codes" in substance)
