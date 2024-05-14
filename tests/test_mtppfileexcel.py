import openpyxl
from mtpp import MTPPData, MTPPFileExcel


INPUT_FILE = "tests/data/sampledata.xlsx"
OUTPUT_FILE = "tests/data/sampledata-out.xlsx"
SHEET = "Sheet1"
RECORDS = [
    {"都道府県": "鹿児島県", "カラム1": "119", "カラム2": "250"},
    {"都道府県": "徳島県", "カラム1": "193", "カラム2": "31"},
    {"都道府県": "大分県", "カラム1": "187", "カラム2": "206"},
    {"都道府県": "宮崎県", "カラム1": "162", "カラム2": "192"},
    {"都道府県": "愛媛県", "カラム1": "89", "カラム2": "236"},
    {"都道府県": "山口県", "カラム1": "94", "カラム2": "235"},
    {"都道府県": "徳島県", "カラム1": "73", "カラム2": "86"},
    {"都道府県": "神奈川県", "カラム1": "207", "カラム2": "103"},
    {"都道府県": "熊本県", "カラム1": "50", "カラム2": "91"},
    {"都道府県": "山梨県", "カラム1": "198", "カラム2": "20"},
    {"都道府県": "富山県", "カラム1": "170", "カラム2": "17"},
    {"都道府県": "高知県", "カラム1": "96", "カラム2": "102"},
    {"都道府県": "鳥取県", "カラム1": "89", "カラム2": "239"},
    {"都道府県": "岐阜県", "カラム1": "27", "カラム2": "198"},
    {"都道府県": "東京都", "カラム1": "175", "カラム2": "201"},
    {"都道府県": "福島県", "カラム1": "136", "カラム2": "49"},
    {"都道府県": "神奈川県", "カラム1": "191", "カラム2": "147"},
    {"都道府県": "宮崎県", "カラム1": "180", "カラム2": "33"},
    {"都道府県": "静岡県", "カラム1": "236", "カラム2": "201"},
    {"都道府県": "滋賀県", "カラム1": "249", "カラム2": "59"},
    {"都道府県": "岡山県", "カラム1": "8", "カラム2": "181"},
    {"都道府県": "静岡県", "カラム1": "11", "カラム2": "188"},
    {"都道府県": "和歌山県", "カラム1": "40", "カラム2": "89"},
    {"都道府県": "千葉県", "カラム1": "252", "カラム2": "106"},
    {"都道府県": "埼玉県", "カラム1": "2", "カラム2": "65"},
]


class TestMTPPFileExcel:
    def test_excel_instance(self):
        target = MTPPFileExcel.read(INPUT_FILE, SHEET)
        assert isinstance(target, MTPPData)

    def test_excel_read_data(self):
        target = MTPPFileExcel.read(INPUT_FILE, SHEET)
        assert target == RECORDS

    def test_excel_write(self):
        data = MTPPData(RECORDS)
        MTPPFileExcel.write(data, OUTPUT_FILE, SHEET)
        workbook = openpyxl.load_workbook(OUTPUT_FILE)
        wworksheet = workbook[SHEET]
        it = wworksheet.values
        headers = next(it)
        records = []
        for row in it:
            record = {}
            for header, column in zip(headers, row):
                record[header] = "" if column is None else str(column)
            records.append(record)
        assert records == RECORDS
