from datetime import datetime
from lxml import objectify, etree

class XmlConverter(object):

    def convert(self, xml):
        return {}

    def convert_to_iso_date(self, date):
        date = datetime.strptime(date, "%Y-%m-%d")
        return date.isoformat()
