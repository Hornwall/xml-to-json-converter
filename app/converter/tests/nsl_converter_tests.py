from .converter_test_case import ConverterTestCase
import os
from ..nsl.nsl_converter import NslConverter
from lxml import objectify, etree

class NslConverterTests(ConverterTestCase):
    def test_returns_one_substance(self):
        self.assertEqual(len(NslConverter().convert(self.xml_obj)), 1)
