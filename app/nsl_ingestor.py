import os
import io
import json_encoder
import file_utils
import config
import zipfile

from lxml import objectify, etree
from converter.nsl.nsl_converter import NslConverter
from converter.nsl.nsl_dictionary_converter import NslDictionaryConverter
from converter.nsl.other.nsl_other_converter import NslOtherConverter

def ingest():
    file_utils.download_and_extract(
            config.NSL_ARCHIVE_URL, 
            config.NSL_DOWNLOAD_LOCATION)

    xml_obj = open_and_objectify(os.path.join(config.NSL_DOWNLOAD_LOCATION, "SEnsl_ssi.xml"))
    nsl_other_xml_obj = open_and_objectify(os.path.join(config.NSL_DOWNLOAD_LOCATION, "SEnsl_other.xml"))

    nsl_dict = NslConverter().convert(xml_obj)
    nsl_other_dict = NslOtherConverter().convert(nsl_other_xml_obj)

    dump_nsl(nsl_dict)
    dump_nsl_other(nsl_other_dict)
    dump_dictionaries()

    file_utils.cleanup(config.NSL_DOWNLOAD_LOCATION)
    file_utils.zipdir(config.NSL_JSON_OUTPUT_PATH, config.NSL_ARCHIVE_NAME)
    file_utils.cleanup(config.NSL_JSON_OUTPUT_PATH)
    file_utils.upload_file(config.NSL_DIFF_UPDATE_URL, config.NSL_ARCHIVE_NAME)
    file_utils.delete_file(config.NSL_ARCHIVE_NAME)

def dump_nsl(nsl_dict):
    for item in nsl_dict:
        filename = ""
        for code in item["substance_codes"]:
            if code["code_system_cv"]["term_id"] == "SENSLIDSENSL":
                filename = code["code"]
                break

        json_encoder.dump_json(item, filename + ".json")

def dump_nsl_other(nsl_other_dict):
    for item in nsl_other_dict:
        json_encoder.dump_json(item, item["se_nsl_id"] + "_other.json")

def dump_dictionaries():
    dictionaries = config.NSL_DICTIONARIES_TO_CONVERT;

    for dictionary in dictionaries:
        dict_obj = open_and_objectify(os.path.join(config.NSL_DOWNLOAD_LOCATION, dictionary + ".xsd"))
        json_encoder.dump_json(NslDictionaryConverter().convert(dict_obj), dictionary + ".json")


def open_and_objectify(path):
    print("objectifying: {path}".format(**locals()))
    xml = open(path)
    xml_string = xml.read().encode("UTF-8")
    return objectify.fromstring(xml_string)

