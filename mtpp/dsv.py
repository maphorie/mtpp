from csv import DictReader, DictWriter
from .core import MTPPData, MTPPFile


#
# MTPPFileDSV クラス
#


# pylint: disable=duplicate-code
class MTPPFileDSV(MTPPFile):
    """
    DSVファイルからの読み込みと書き込みを行うクラス
    """

    @staticmethod
    def read(file: str, *_, **kwargs) -> MTPPData:
        """
        DSVファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): DSVファイル名
        encoding (str | None): DSVファイルのエンコーディング

        Returns:
        MTPPDataクラスのインスタンス
        """
        if "encoding" not in kwargs:
            raise KeyError
        encoding = kwargs.pop("encoding")

        if "dialect" not in kwargs:
            raise KeyError
        dialect = kwargs.pop("dialect")

        with open(file, "r", encoding=encoding) as f:
            reader = DictReader(f, dialect=dialect)
            records = list(reader)

        return MTPPData(records)

    @staticmethod
    def write(data: MTPPData, file: str, *_, **kwargs) -> None:
        """
        DSVファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): DSVファイル名
        encoding (str | None): DSVファイルのエンコーディング
        """
        if "encoding" not in kwargs:
            raise KeyError
        encoding = kwargs.pop("encoding")

        if "dialect" not in kwargs:
            raise KeyError
        dialect = kwargs.pop("dialect")

        rows = data.rows
        fieldnames = rows[0].keys()

        with open(file, "w", encoding=encoding) as f:
            writer = DictWriter(f, fieldnames, dialect=dialect)
            writer.writeheader()
            writer.writerows(rows)
