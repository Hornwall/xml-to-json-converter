from .converter_test_case import ConverterTestCase
from ..nsl.other.nsl_other_converter import NslOtherConverter


class NslOtherConverterTests(ConverterTestCase):
    def test_returns_one_substance(self):
        self.assertEqual(len(NslOtherConverter().convert(self.nsl_other_xml_obj)), 1)
