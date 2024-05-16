from csv import DictReader
from mtpp import MTPPData, MTPPFileCSV
from .constant import (
    INPUT_FILE_CSV_UTF8,
    INPUT_FILE_CSV_SJIS,
    OUTPUT_FILE_CSV_UTF8,
    OUTPUT_FILE_CSV_SJIS,
    ENCODING_UTF8,
    ENCODING_SJIS,
    RECORDS,
)


class TestMTPPFileCSV:
    def test_csv_instance_utf8(self):
        target = MTPPFileCSV.read(INPUT_FILE_CSV_UTF8, encoding=ENCODING_UTF8)
        assert isinstance(target, MTPPData)

    def test_csv_instance_sjis(self):
        target = MTPPFileCSV.read(INPUT_FILE_CSV_SJIS, encoding=ENCODING_SJIS)
        assert isinstance(target, MTPPData)

    def test_csv_read_utf8(self):
        target = MTPPFileCSV.read(INPUT_FILE_CSV_UTF8, encoding=ENCODING_UTF8)
        assert target == RECORDS

    def test_csv_read_sjis(self):
        target = MTPPFileCSV.read(INPUT_FILE_CSV_SJIS, encoding=ENCODING_SJIS)
        assert target == RECORDS

    def test_csv_write_utf8(self):
        data = MTPPData(RECORDS)
        MTPPFileCSV.write(OUTPUT_FILE_CSV_UTF8, data, encoding=ENCODING_UTF8)
        with open(OUTPUT_FILE_CSV_UTF8, encoding=ENCODING_UTF8) as f:
            reader = DictReader(f)
            records = list(reader)
        assert records == RECORDS

    def test_csv_write_sjis(self):
        data = MTPPData(RECORDS)
        MTPPFileCSV.write(OUTPUT_FILE_CSV_SJIS, data, encoding=ENCODING_SJIS)
        with open(OUTPUT_FILE_CSV_SJIS, encoding=ENCODING_SJIS) as f:
            reader = DictReader(f)
            records = list(reader)
        assert records == RECORDS
