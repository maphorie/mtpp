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
        file (str): TSVファイル名

        Returns:
        MTPPDataクラスのインスタンス
        """
        kwargs["dialect"] = "excel-tab"

        return super().read(file, *args, **kwargs)

    @classmethod
    def write(cls, file: str, data: MTPPData, *args, **kwargs) -> None:
        """
        TSVファイルにエクスポート

        Parameters:
        file (str): TSVファイル名
        data (MTPPData) MTPPDataクラスのインスタンス
        """
        kwargs["dialect"] = "excel-tab"

        super().write(file, data, *args, **kwargs)
