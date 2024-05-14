import csv
from typing import Optional
from .core import MTPPData, MTPPFile


#
# MTPPFileCSV クラス
#


class MTPPFileCSV(MTPPFile):
    """
    CSVファイルからの読み込みと書き込みを行うクラス
    """

    @staticmethod
    def read(file: str, encoding: Optional[str] = None) -> MTPPData:
        """
        CSVファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): CSVファイル名
        encoding (str | None): CSVファイルのエンコーディング

        Returns:
        MTPPDataクラスのインスタンス
        """
        with open(file, "r", encoding=encoding) as f:
            reader = csv.DictReader(f)
            records = list(reader)

        return MTPPData(records)

    @staticmethod
    def write(data: MTPPData, file: str, encoding: Optional[str] = None) -> None:
        """
        CSVファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): CSVファイル名
        encoding (str | None): CSVファイルのエンコーディング
        """
        rows = data.rows
        fieldnames = rows[0].keys()

        with open(file, "w", encoding=encoding) as f:
            writer = csv.DictWriter(f, fieldnames)
            writer.writeheader()
            writer.writerows(rows)
