import unittest
import os
from lxml import objectify, etree
from ..nsl.nsl_converter import NslConverter

class ConverterTestCase(unittest.TestCase):
    example_path = os.path.dirname(os.path.abspath(__file__)) + "/example_data/"
    xml_obj = ""

    def setUp(self):
        xml_file = open(self.example_path + "substance.xml")
        xml_data = xml_file.read()
        xml_file.close()
        self.xml_obj = objectify.fromstring(xml_data)
        pass

    def _convert_substance(self):
        return NslConverter().convert(self.xml_obj)
