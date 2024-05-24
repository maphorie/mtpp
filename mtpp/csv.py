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
        file (str): CSVファイル名

        Returns:
        MTPPDataクラスのインスタンス
        """
        kwargs["dialect"] = "excel"

        return super().read(file, *args, **kwargs)

    @classmethod
    def write(cls, file: str, data: MTPPData, *args, **kwargs) -> None:
        """
        CSVファイルにエクスポート

        Parameters:
        file (str): CSVファイル名
        data (MTPPData) MTPPDataクラスのインスタンス
        """
        kwargs["dialect"] = "excel"

        super().write(file, data, *args, **kwargs)
