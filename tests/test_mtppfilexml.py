from mtpp import MTPPData, MTPPFileXML
from .constant import (
    INPUT_FILE_XML_UTF8,
    INPUT_FILE_XML_SJIS,
    ENCODING_UTF8,
    ENCODING_SJIS,
    RECORDS,
)


class TestMTPPFileXML:
    def test_xml_instance(self):
        target = MTPPFileXML.read(INPUT_FILE_XML_UTF8, ENCODING_UTF8)
        assert isinstance(target, MTPPData)

    def test_xml_read_utf8(self):
        target = MTPPFileXML.read(INPUT_FILE_XML_UTF8, ENCODING_UTF8)
        assert target == RECORDS

    def test_xml_read_sjis(self):
        target = MTPPFileXML.read(INPUT_FILE_XML_SJIS, ENCODING_SJIS)
        assert target == RECORDS
