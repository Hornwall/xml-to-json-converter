from lxml import objectify, etree
import simplejson as json
from converter.nsl.nsl_converter import NslConverter

import sys

xml = open("SEnsl_ssi.xml")
xml_string = xml.read()
xml_obj = objectify.fromstring(xml_string)

nsl_dict = NslConverter().convert(xml_obj)

count = 0
for item in nsl_dict:
    with open('json/' + str(count) + ".json", 'w') as outfile:
        json.dump(item, outfile)
    count += 1
