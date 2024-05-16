INPUT_FILE_CSV_UTF8 = "tests/data/sampledata-utf8.csv"
INPUT_FILE_CSV_SJIS = "tests/data/sampledata-sjis.csv"
INPUT_FILE_TSV_UTF8 = "tests/data/sampledata-utf8.tsv"
INPUT_FILE_TSV_SJIS = "tests/data/sampledata-sjis.tsv"
INPUT_FILE_XML_UTF8 = "tests/data/sampledata-utf8.xml"
INPUT_FILE_XML_SJIS = "tests/data/sampledata-sjis.xml"
INPUT_FILE_EXCEL = "tests/data/sampledata.xlsx"

OUTPUT_FILE_CSV_UTF8 = "tests/data/sampledata-out-utf8.csv"
OUTPUT_FILE_CSV_SJIS = "tests/data/sampledata-out-sjis.csv"
OUTPUT_FILE_TSV_UTF8 = "tests/data/sampledata-out-utf8.tsv"
OUTPUT_FILE_TSV_SJIS = "tests/data/sampledata-out-sjis.tsv"
OUTPUT_FILE_EXCEL = "tests/data/sampledata-out.xlsx"

ENCODING_UTF8 = "UTF-8"
ENCODING_SJIS = "Shift_JIS"

EXCEL_SHEET = "Sheet1"

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
    {"都道府県": "静岡県", "カラム1": "11", "カラム2": "188"},
    {"都道府県": "滋賀県", "カラム1": "249", "カラム2": "59"},
    {"都道府県": "岡山県", "カラム1": "8", "カラム2": "181"},
    {"都道府県": "静岡県", "カラム1": "236", "カラム2": "201"},
    {"都道府県": "和歌山県", "カラム1": "40", "カラム2": "89"},
    {"都道府県": "千葉県", "カラム1": "252", "カラム2": "106"},
    {"都道府県": "静岡県", "カラム1": "2", "カラム2": "65"},
]

PYTHON_BEFORE_CALL = RECORDS
PYTHON_AFTER_CALL = [
    {"都道府県": "鹿児島県", "カラム1": "119", "カラム2": "250"},
    {"都道府県": "徳島県", "カラム1": "193", "カラム2": "31"},
    {"都道府県": "大分県", "カラム1": "187", "カラム2": "206"},
    {"都道府県": "宮崎県", "カラム1": "162", "カラム2": "192"},
    {"都道府県": "愛媛県", "カラム1": "89", "カラム2": "236"},
    {"都道府県": "山口県", "カラム1": "94", "カラム2": "235"},
    {"都道府県": "神奈川県", "カラム1": "207", "カラム2": "103"},
    {"都道府県": "熊本県", "カラム1": "50", "カラム2": "91"},
    {"都道府県": "山梨県", "カラム1": "198", "カラム2": "20"},
    {"都道府県": "富山県", "カラム1": "170", "カラム2": "17"},
    {"都道府県": "高知県", "カラム1": "96", "カラム2": "102"},
    {"都道府県": "鳥取県", "カラム1": "89", "カラム2": "239"},
    {"都道府県": "岐阜県", "カラム1": "27", "カラム2": "198"},
    {"都道府県": "東京都", "カラム1": "175", "カラム2": "201"},
    {"都道府県": "福島県", "カラム1": "136", "カラム2": "49"},
    {"都道府県": "静岡県", "カラム1": "11", "カラム2": "188"},
    {"都道府県": "静岡県", "カラム1": "236", "カラム2": "201"},
    {"都道府県": "滋賀県", "カラム1": "249", "カラム2": "59"},
    {"都道府県": "岡山県", "カラム1": "8", "カラム2": "181"},
    {"都道府県": "和歌山県", "カラム1": "40", "カラム2": "89"},
    {"都道府県": "千葉県", "カラム1": "252", "カラム2": "106"},
]

PANDAS_BEFORE_CALL = RECORDS
PANDAS_AFTER_CALL = [
    {"都道府県": "鹿児島県", "カラム1": "119", "カラム2": "250", "カラム比": "0.476"},
    {"都道府県": "徳島県", "カラム1": "193", "カラム2": "31", "カラム比": "6.225806451612903"},
    {"都道府県": "大分県", "カラム1": "187", "カラム2": "206", "カラム比": "0.9077669902912622"},
    {"都道府県": "宮崎県", "カラム1": "162", "カラム2": "192", "カラム比": "0.84375"},
    {"都道府県": "愛媛県", "カラム1": "89", "カラム2": "236", "カラム比": "0.3771186440677966"},
    {"都道府県": "山口県", "カラム1": "94", "カラム2": "235", "カラム比": "0.4"},
    {"都道府県": "徳島県", "カラム1": "73", "カラム2": "86", "カラム比": "0.8488372093023255"},
    {"都道府県": "神奈川県", "カラム1": "207", "カラム2": "103", "カラム比": "2.0097087378640777"},
    {"都道府県": "熊本県", "カラム1": "50", "カラム2": "91", "カラム比": "0.5494505494505495"},
    {"都道府県": "山梨県", "カラム1": "198", "カラム2": "20", "カラム比": "9.9"},
    {"都道府県": "富山県", "カラム1": "170", "カラム2": "17", "カラム比": "10.0"},
    {"都道府県": "高知県", "カラム1": "96", "カラム2": "102", "カラム比": "0.9411764705882353"},
    {"都道府県": "鳥取県", "カラム1": "89", "カラム2": "239", "カラム比": "0.3723849372384937"},
    {"都道府県": "岐阜県", "カラム1": "27", "カラム2": "198", "カラム比": "0.13636363636363635"},
    {"都道府県": "東京都", "カラム1": "175", "カラム2": "201", "カラム比": "0.8706467661691543"},
    {"都道府県": "福島県", "カラム1": "136", "カラム2": "49", "カラム比": "2.7755102040816326"},
    {"都道府県": "神奈川県", "カラム1": "191", "カラム2": "147", "カラム比": "1.2993197278911566"},
    {"都道府県": "宮崎県", "カラム1": "180", "カラム2": "33", "カラム比": "5.454545454545454"},
    {"都道府県": "静岡県", "カラム1": "11", "カラム2": "188", "カラム比": "0.05851063829787234"},
    {"都道府県": "滋賀県", "カラム1": "249", "カラム2": "59", "カラム比": "4.220338983050848"},
    {"都道府県": "岡山県", "カラム1": "8", "カラム2": "181", "カラム比": "0.04419889502762431"},
    {"都道府県": "静岡県", "カラム1": "236", "カラム2": "201", "カラム比": "1.1741293532338308"},
    {"都道府県": "和歌山県", "カラム1": "40", "カラム2": "89", "カラム比": "0.449438202247191"},
    {"都道府県": "千葉県", "カラム1": "252", "カラム2": "106", "カラム比": "2.3773584905660377"},
    {"都道府県": "静岡県", "カラム1": "2", "カラム2": "65", "カラム比": "0.03076923076923077"},
]
