import sys
from csv import DictReader, DictWriter
from .core import MTPPData, MTPPFile


#
# MTPPFileDSV クラス
#


class MTPPFileDSV(MTPPFile):
    """
    DSV(CSV, TSV)ファイルからの読み込みと書き込みを行うクラス
    """

    @classmethod
    def read(cls, file: str, *args, **kwargs) -> MTPPData:
        """
        DSVファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): DSVファイル名
        encoding (str | None): DSVファイルのエンコーディング

        Returns:
        MTPPDataクラスのインスタンス
        """
        encoding = kwargs.pop("encoding") if "encoding" in kwargs else sys.getfilesystemencoding()

        if "dialect" not in kwargs:
            raise KeyError
        dialect = kwargs.pop("dialect")

        with open(file, "r", encoding=encoding) as f:
            reader = DictReader(f, dialect=dialect)
            records = list(reader)

        return MTPPData(records)

    @classmethod
    def write(cls, data: MTPPData, file: str, *args, **kwargs) -> None:
        """
        DSVファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): DSVファイル名
        encoding (str | None): DSVファイルのエンコーディング
        """
        encoding = kwargs.pop("encoding") if "encoding" in kwargs else sys.getfilesystemencoding()

        if "dialect" not in kwargs:
            raise KeyError
        dialect = kwargs.pop("dialect")

        rows = data.rows
        fieldnames = rows[0].keys()

        with open(file, "w", encoding=encoding) as f:
            writer = DictWriter(f, fieldnames, dialect=dialect)
            writer.writeheader()
            writer.writerows(rows)
