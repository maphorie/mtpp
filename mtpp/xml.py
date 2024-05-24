import sys
from xml.etree import ElementTree

from .core import MTPPData, MTPPFile


#
# MTPPFileXML クラス
#


class MTPPFileXML(MTPPFile):
    """
    XMLファイルからの読み込みと書き込みを行うクラス
    """

    @classmethod
    def read(cls, file: str, *args, **kwargs) -> MTPPData:
        """
        XMLファイルからMTPPDataクラスのインスタンスを作成

        Parameters:
        file (str): XMLファイル名

        Returns:
        MTPPDataクラスのインスタンス
        """
        encoding = kwargs.pop("encoding") if "encoding" in kwargs else sys.getfilesystemencoding()

        with open(file, "r", encoding=encoding) as f:
            content = f.read()

        tree = ElementTree.fromstring(content)
        rows = [dict(element.items()) for element in tree]

        return MTPPData(rows)

    @classmethod
    def write(cls, file: str, data: MTPPData, *args, **kwargs) -> None:
        """
        XMLファイルにエクスポート

        Parameters:
        file (str): XMLファイル名
        data (MTPPData) MTPPDataクラスのインスタンス
        """
        raise NotImplementedError
