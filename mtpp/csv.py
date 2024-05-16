from .core import MTPPData
from .dsv import MTPPFileDSV


#
# MTPPFileCSV クラス
#


class MTPPFileCSV(MTPPFileDSV):
    """
    CSVファイルからの読み込みと書き込みを行うクラス
    """

    @classmethod
    def read(cls, file: str, *args, **kwargs) -> MTPPData:
        """
        CSVファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): CSVファイル名
        encoding (str | None): CSVファイルのエンコーディング

        Returns:
        MTPPDataクラスのインスタンス
        """
        kwargs["dialect"] = "excel"

        return super().read(file, *args, **kwargs)

    @classmethod
    def write(cls, data: MTPPData, file: str, *args, **kwargs) -> None:
        """
        CSVファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): CSVファイル名
        encoding (str | None): CSVファイルのエンコーディング
        """
        kwargs["dialect"] = "excel"

        super().write(data, file, *args, **kwargs)
