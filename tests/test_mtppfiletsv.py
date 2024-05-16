from csv import DictReader
from mtpp import MTPPData, MTPPFileTSV
from .constant import (
    INPUT_FILE_TSV_UTF8,
    INPUT_FILE_TSV_SJIS,
    OUTPUT_FILE_TSV_UTF8,
    OUTPUT_FILE_TSV_SJIS,
    ENCODING_UTF8,
    ENCODING_SJIS,
    RECORDS,
)


class TestMTPPFileTSV:
    def test_tsv_instance_utf8(self):
        target = MTPPFileTSV.read(INPUT_FILE_TSV_UTF8, encoding=ENCODING_UTF8)
        assert isinstance(target, MTPPData)

    def test_tsv_instance_sjis(self):
        target = MTPPFileTSV.read(INPUT_FILE_TSV_SJIS, encoding=ENCODING_SJIS)
        assert isinstance(target, MTPPData)

    def test_tsv_read_utf8(self):
        target = MTPPFileTSV.read(INPUT_FILE_TSV_UTF8, encoding=ENCODING_UTF8)
        assert target == RECORDS

    def test_tsv_read_sjis(self):
        target = MTPPFileTSV.read(INPUT_FILE_TSV_SJIS, encoding=ENCODING_SJIS)
        assert target == RECORDS

    def test_tsv_write_utf8(self):
        data = MTPPData(RECORDS)
        MTPPFileTSV.write(OUTPUT_FILE_TSV_UTF8, data, encoding=ENCODING_UTF8)
        with open(OUTPUT_FILE_TSV_UTF8, encoding=ENCODING_UTF8) as f:
            reader = DictReader(f, dialect="excel-tab")
            records = list(reader)
        assert records == RECORDS

    def test_tsv_write_sjis(self):
        data = MTPPData(RECORDS)
        MTPPFileTSV.write(OUTPUT_FILE_TSV_SJIS, data, encoding=ENCODING_SJIS)
        with open(OUTPUT_FILE_TSV_SJIS, encoding=ENCODING_SJIS) as f:
            reader = DictReader(f, dialect="excel-tab")
            records = list(reader)
        assert records == RECORDS
