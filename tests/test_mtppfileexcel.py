import openpyxl

from mtpp import MTPPData, MTPPFileExcel

from .constant import INPUT_FILE_EXCEL, OUTPUT_FILE_EXCEL, EXCEL_SHEET, RECORDS


class TestMTPPFileExcel:
    def test_excel_instance(self):
        target = MTPPFileExcel.read(INPUT_FILE_EXCEL, EXCEL_SHEET)
        assert isinstance(target, MTPPData)

    def test_excel_read_data(self):
        target = MTPPFileExcel.read(INPUT_FILE_EXCEL, EXCEL_SHEET)
        assert target == RECORDS

    def test_excel_write(self):
        data = MTPPData(RECORDS)
        MTPPFileExcel.write(OUTPUT_FILE_EXCEL, data, EXCEL_SHEET)
        workbook = openpyxl.load_workbook(OUTPUT_FILE_EXCEL)
        wworksheet = workbook[EXCEL_SHEET]
        it = wworksheet.values
        headers = next(it)
        records = []
        for row in it:
            record = {}
            for header, column in zip(headers, row):
                record[header] = "" if column is None else str(column)
            records.append(record)
        assert records == RECORDS
