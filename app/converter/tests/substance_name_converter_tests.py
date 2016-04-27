from .converter_test_case import ConverterTestCase
import os
from ..nsl.substance_name_converter import SubstanceNameConverter
from lxml import objectify, etree

class SubstanceNameConverterTests(ConverterTestCase):

    def test_substance_name_is_expected_to_have_name(self):
        substance_names = SubstanceNameConverter().convert(self.get_substance_names_xml_object())
        self.assertTrue("name" in substance_names[0])

    def test_substance_name_is_expected_to_have_type_cv(self):
        substance_names = SubstanceNameConverter().convert(self.get_substance_names_xml_object())
        self.assertTrue("language_cv" in substance_names[0])

    def test_substance_name_is_expected_to_have_type_cv(self):
        substance_names = SubstanceNameConverter().convert(self.get_substance_names_xml_object())
        self.assertTrue("substance_name_type_cv" in substance_names[0])

    def test_substance_has_two_names(self):
        substance_names = SubstanceNameConverter().convert(self.get_substance_names_xml_object())
        self.assertEqual(len(substance_names), 4)

    def get_substance_names_xml_object(self):
        return self.nsl_xml_obj.substance.common["substance-names"]

