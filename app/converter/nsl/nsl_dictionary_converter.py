from lxml import objectify, etree
from operator import itemgetter
from ..xml_converter import XmlConverter

class NslDictionaryConverter(XmlConverter):
    def convert(self, xml):
        dictionary_entries = []
        for entry in xml["simpleType"]["restriction"].iterchildren():
            dictionary_entries.append(self.convert_entry(entry))
        return dictionary_entries

    def convert_entry(self, xml):
        entry = {}
        entry["value"] = xml.attrib["value"]
        if "appinfo" in xml["annotation"]:
            entry["app_info"] = xml["annotation"]["appinfo"].text
        else:
            entry["app_info"] = None

        entry["documentation"] = self.convert_entry_documentation(xml["annotation"])
        return entry

    def convert_entry_documentation(self, xml):
        documentation = []

        for doc in xml["documentation"]:
            entry = {}
            entry["lang"] = doc.attrib["{http://www.w3.org/XML/1998/namespace}lang"]
            entry["value"] = doc.text
            documentation.append(entry)
        return sorted(documentation, key = itemgetter("lang", "value"))
