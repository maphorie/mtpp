import openpyxl
from openpyxl import Workbook
from .core import MTPPData, MTPPFile


#
# MTPPFileExcel クラス
#


class MTPPFileExcel(MTPPFile):
    """
    Excelファイルからの読み込みと書き込みを行うクラス
    """

    @classmethod
    def read(cls, file: str, *args, **kwargs) -> MTPPData:
        """
        ExcelファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): Excelファイル名
        sheet_name (str): Excelファイルのシート名

        Returns:
        MTPPDataクラスのインスタンス
        """
        sheet_name = kwargs.pop("sheet_name") if "sheet_name" in kwargs else "Sheet1"

        workbook = openpyxl.load_workbook(file)
        wworksheet = workbook[sheet_name]
        it = wworksheet.values

        headers = next(it)
        data = []
        for row in it:
            record = {}
            for header, column in zip(headers, row):
                record[header] = "" if column is None else str(column)
            data.append(record)

        return MTPPData(data)

    @classmethod
    def write(cls, file: str, data: MTPPData, *args, **kwargs) -> None:
        """
        Excelファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): Excelファイル名
        sheet_name (str): Excelファイルのシート名
        """
        sheet_name = kwargs.pop("sheet_name") if "sheet_name" in kwargs else "Sheet1"

        workbook = Workbook()
        wworksheet = workbook.active
        wworksheet.title = sheet_name

        rows = data.rows
        headers = rows[0].keys()

        wworksheet.append(list(headers))
        for row in rows:
            row_data = [row[header] for header in headers]
            wworksheet.append(row_data)

        workbook.save(file)
