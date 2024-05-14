import csv
from typing import Optional
from .core import MTPPData, MTPPFile


#
# MTPPFileTSV クラス
#


class MTPPFileTSV(MTPPFile):
    """
    TSVファイルからの読み込みと書き込みを行うクラス
    """

    @staticmethod
    def read(file: str, encoding: Optional[str] = None) -> MTPPData:
        """
        TSVファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): TSVファイル名
        encoding (str | None): TSVファイルのエンコーディング

        Returns:
        MTPPDataクラスのインスタンス
        """
        with open(file, "r", encoding=encoding) as f:
            reader = csv.DictReader(f, dialect="excel-tab")
            records = list(reader)

        return MTPPData(records)

    @staticmethod
    def write(data: MTPPData, file: str, encoding: Optional[str] = None) -> None:
        """
        TSVファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): TSVファイル名
        encoding (str | None): TSVファイルのエンコーディング
        """
        rows = data.rows
        fieldnames = rows[0].keys()

        with open(file, "w", encoding=encoding) as f:
            writer = csv.DictWriter(f, fieldnames, dialect="excel-tab")
            writer.writeheader()
            writer.writerows(rows)
