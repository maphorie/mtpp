from .core import MTPPData
from .dsv import MTPPFileDSV


#
# MTPPFileTSV クラス
#


class MTPPFileTSV(MTPPFileDSV):
    """
    TSVファイルからの読み込みと書き込みを行うクラス
    """

    @classmethod
    def read(cls, file: str, *args, **kwargs) -> MTPPData:
        """
        TSVファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): TSVファイル名
        encoding (str | None): TSVファイルのエンコーディング

        Returns:
        MTPPDataクラスのインスタンス
        """
        kwargs["dialect"] = "excel-tab"

        return super().read(file, *args, **kwargs)

    @classmethod
    def write(cls, data: MTPPData, file: str, *args, **kwargs) -> None:
        """
        TSVファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): TSVファイル名
        encoding (str | None): TSVファイルのエンコーディング
        """
        kwargs["dialect"] = "excel-tab"

        super().write(data, file, *args, **kwargs)
