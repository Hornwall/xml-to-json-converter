from datetime import datetime
from lxml import objectify, etree
from pprint import pformat

import hashlib

class XmlConverter(object):

    def convert(self, xml):
        return {}

    def convert_to_iso_date(self, date):
        date = datetime.strptime(date, "%Y-%m-%d")
        return date.isoformat()

    def hash_dict(self, dictionary):
        return str(hashlib.sha1(pformat(dictionary).encode("utf-8")))
