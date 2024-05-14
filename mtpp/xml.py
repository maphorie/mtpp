from typing import Optional
from xml.etree import ElementTree
from .core import MTPPData, MTPPFile


#
# MTPPFileXML クラス
#


class MTPPFileXML(MTPPFile):
    """
    XMLファイルからの読み込みと書き込みを行うクラス
    """

    @staticmethod
    def read(file: str, encoding: Optional[str] = None) -> MTPPData:
        """
        XMLファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        filepath (str): XMLファイル名
        encoding (str | None): XMLファイルのエンコーディング

        Returns:
        MTPPDataクラスのインスタンス
        """
        with open(file, "r", encoding=encoding) as f:
            content = f.read()

        tree = ElementTree.fromstring(content)
        rows = [dict(element.items()) for element in tree]

        return MTPPData(rows)

    @staticmethod
    def write(data: MTPPData, file: str, encoding: Optional[str] = None) -> None:
        """
        XMLファイルにエクスポート

        Parameters:
        data (MTPPData) MTPPDataクラスのインスタンス
        filepath (str): XMLファイル名
        encoding (str | None): XMLファイルのエンコーディング
        """
        raise NotImplementedError
