import os
import zipfile
import sys
import simplejson as json

from lxml import objectify, etree
from converter.nsl.nsl_converter import NslConverter
from converter.nsl.other.nsl_other_converter import NslOtherConverter



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

        with open(output_dir + filename + ".json", 'w') as outfile:
            json.dump(item, outfile, sort_keys=True)

    for item in nsl_other_dict:
        with open(output_dir + item["se_nsl_id"] + "_other.json", "w") as outfile:
            json.dump(item, outfile, sort_keys=True)

def cleanup(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(directory)

def zipdir(path, zip_file):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip_file.write(os.path.join(root, file), file)

if __name__ == '__main__':
    convert_nsl("", "json/")
    zipf = zipfile.ZipFile('nsl.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('json/', zipf)
    zipf.close()
    cleanup("json/")
