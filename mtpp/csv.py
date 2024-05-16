from .core import MTPPData
from .dsv import MTPPFileDSV


#
# MTPPFileCSV クラス
#


class MTPPFileCSV(MTPPFileDSV):
    """
    CSVファイルからの読み込みと書き込みを行うクラス
    """

    @staticmethod
    def read(file: str, *args, **kwargs) -> MTPPData:
        """
        CSVファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): CSVファイル名
        encoding (str | None): CSVファイルのエンコーディング

        Returns:
        MTPPDataクラスのインスタンス
        """
        kwargs["dialect"] = "excel"

        return MTPPFileDSV.read(file, *args, **kwargs)

    @staticmethod
    def write(data: MTPPData, file: str, *args, **kwargs) -> None:
        """
        CSVファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): CSVファイル名
        encoding (str | None): CSVファイルのエンコーディング
        """
        kwargs["dialect"] = "excel"

        MTPPFileDSV.write(data, file, *args, **kwargs)
