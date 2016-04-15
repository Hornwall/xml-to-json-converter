import os
import zipfile
import sys

from lxml import objectify, etree
from converter.nsl.nsl_converter import NslConverter
from converter.nsl.other.nsl_other_converter import NslOtherConverter

import json_encoder
import config
import file_utils



def convert_nsl(input_dir, output_dir):
    xml = open(input_dir + "SEnsl_ssi.xml")
    xml_string = xml.read()
    xml_obj = objectify.fromstring(xml_string)

    nsl_other_xml_string = open(input_dir + "SEnsl_other.xml").read()
    nsl_other_xml_obj = objectify.fromstring(nsl_other_xml_string)


    nsl_dict = NslConverter().convert(xml_obj)
    nsl_other_dict = NslOtherConverter().convert(nsl_other_xml_obj)

    if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    for item in nsl_dict:
        filename = ""
        for code in item["substance_codes"]:
            if code["code_system"] == "SENSLIDSENSL":
                filename = code["code"]
                break

        json_encoder.dump_json(item, filename + ".json")

    for item in nsl_other_dict:
        json_encoder.dump_json(item, item["se_nsl_id"] + "_other.json")



if __name__ == '__main__':
    convert_nsl("", "json/")
    file_utils.zipdir(config.NSL_JSON_OUTPUT_PATH, "nsl.zip")
    file_utils.cleanup(config.NSL_JSON_OUTPUT_PATH)
