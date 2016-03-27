from lxml import objectify, etree
import simplejson as json
from converter.nsl.nsl_converter import NslConverter
from converter.nsl.other.nsl_other_converter import NslOtherConverter

import sys

xml = open("SEnsl_ssi.xml")
xml_string = xml.read()
xml_obj = objectify.fromstring(xml_string)

nsl_other_xml_string = open("SEnsl_other.xml").read()
nsl_other_xml_obj = objectify.fromstring(nsl_other_xml_string)


nsl_dict = NslConverter().convert(xml_obj)
nsl_other_dict = NslOtherConverter().convert(nsl_other_xml_obj)

for item in nsl_dict:
    filename = ""
    for code in item["substance_codes"]:
        if code["code_system"] == "SENSLIDSENSL":
            filename = code["code"]
            break

    with open('json/' + filename + ".json", 'w') as outfile:
        json.dump(item, outfile, sort_keys=True)

for item in nsl_other_dict:
    with open("json/other/" + item["se_nsl_id"] + ".json", "w") as outfile:
        json.dump(item, outfile, sort_keys=True)
