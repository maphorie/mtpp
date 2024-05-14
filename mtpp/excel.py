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

    @staticmethod
    def read(file: str, sheet_name: str = "Sheet1") -> MTPPData:
        """
        ExcelファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): Excelファイル名
        sheet_name (str): Excelファイルのシート名

        Returns:
        MTPPDataクラスのインスタンス
        """
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

    @staticmethod
    def write(data: MTPPData, file: str, sheet_name: str = "Sheet1") -> None:
        """
        Excelファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): Excelファイル名
        sheet_name (str): Excelファイルのシート名
        """
        workbook = Workbook()
        wworksheet = workbook.active
        wworksheet.title = sheet_name  # type: ignore

        rows = data.rows
        headers = rows[0].keys()

        wworksheet.append(list(headers))  # type: ignore
        for row in rows:
            row_data = [row[header] for header in headers]
            wworksheet.append(row_data)  # type: ignore

        workbook.save(file)
