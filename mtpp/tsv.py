from .core import MTPPData
from .dsv import MTPPFileDSV


#
# MTPPFileTSV クラス
#


class MTPPFileTSV(MTPPFileDSV):
    """
    TSVファイルからの読み込みと書き込みを行うクラス
    """

    @staticmethod
    def read(file: str, *args, **kwargs) -> MTPPData:
        """
        TSVファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): TSVファイル名
        encoding (str | None): TSVファイルのエンコーディング

        Returns:
        MTPPDataクラスのインスタンス
        """
        kwargs["dialect"] = "excel-tab"

        return MTPPFileDSV.read(file, *args, **kwargs)

    @staticmethod
    def write(data: MTPPData, file: str, *args, **kwargs) -> None:
        """
        TSVファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): TSVファイル名
        encoding (str | None): TSVファイルのエンコーディング
        """
        kwargs["dialect"] = "excel-tab"

        MTPPFileDSV.write(data, file, *args, **kwargs)
