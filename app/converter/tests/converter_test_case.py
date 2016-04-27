import unittest
import os
from lxml import objectify, etree
from ..nsl.nsl_converter import NslConverter

class ConverterTestCase(unittest.TestCase):
    example_path = os.path.dirname(os.path.abspath(__file__)) + "/example_data/"
    nsl_xml_obj = ""
    nsl_other_xml_obj = ""
    nsl_dictionary_xml_obj = ""

    def setUp(self):
        self.nsl_xml_obj = self.__load_xml("substance.xml")
        self.nsl_other_xml_obj = self.__load_xml("substance_other.xml")
        self.nsl_dictionary_xml_obj = self.__load_xml("narcclass-lx.xsd")
        pass

    def __load_xml(self, input_file):
        xml_file = open(self.example_path + input_file)
        xml_data = xml_file.read().encode("UTF-8")
        xml_file.close()
        return objectify.fromstring(xml_data)


    def _convert_substance(self):
        return NslConverter().convert(self.xml_obj)
