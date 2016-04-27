from .converter_test_case import ConverterTestCase
import os
from ..nsl.nsl_dictionary_converter import NslDictionaryConverter
from lxml import objectify, etree

class NslDictionaryConverterTests(ConverterTestCase):
    def test_returns_nine_dictionary_entries(self):
        self.assertEqual(len(self.convert_dictionary()), 9)

    def test_dictionary_is_expected_to_have_value(self):
        self.assertTrue("value" in self.convert_dictionary()[0])

    def test_dictionary_is_expected_to_have_app_info(self):
        self.assertTrue("app_info" in self.convert_dictionary()[0])

    def test_dictionary_is_expected_to_have_documentation(self):
        self.assertTrue("documentation" in self.convert_dictionary()[0])

    def test_documentation_is_expected_to_have_two_entries(self):
        self.assertEqual(len(self.convert_dictionary()[0]["documentation"]), 2)

    def test_documentation_is_expected_to_have_lang(self):
        self.assertTrue("lang" in self.convert_dictionary()[0]["documentation"][0])

    def test_documentation_is_expected_to_have_lang(self):
        self.assertTrue("value" in self.convert_dictionary()[0]["documentation"][0])

    def convert_dictionary(self):
        return NslDictionaryConverter().convert(self.nsl_dictionary_xml_obj)

