"""
mtppモジュール


Pandasモジュールでの処理とPythonスクリプトでの処理を協調できるようにする

それぞれの処理はMTPPPandasクラス，MTPPPythonクラスで行う
  - Pandasモジュールを使った処理はMTPPPandasクラス
  - Pythonスクリプトを使った処理はMTPPPythonクラス

各クラスのデータのやり取りにMTPPDataデータクラスを用いる

MTPPPandasクラスとMTPPPythonクラスには__call__メソッドがあり
PandasおよびPythonスクリプトでの処理は
クロージャ(関数，メソッド，ラムダ関数)をつくり__call__メソッドに渡して行う

ファイルの入出力はMTPPFileCSVクラス，MTPPFileExcelクラスで行う
  - CSVファイルはMTPPFileCSVクラス
  - ExcelファイルはMTPPFileExcelクラス
"""


import copy
import math
from pandas import DataFrame


#
# MTPPData クラス
#


class MTPPData:
    """
    MTPPPandasクラスとMTPPPythonクラスとをやり取りするためのデータ

    Attributes:
    data_frame (DataFrame): MTPPPandasクラスとやり取りするためのデータ
    rows (list[dict[str, str]]): MTPPPythonクラスとやり取りするためのデータ
    """

    def __init__(self, value: object) -> None:
        if isinstance(value, list):
            rows = copy.deepcopy(value)
            self._data_frame = DataFrame.from_dict(rows)  # type: ignore
            self._rows = rows
        elif isinstance(value, DataFrame):
            data_frame = copy.deepcopy(value)
            self._data_frame = data_frame
            self._rows = data_frame.to_dict("records")
        else:
            raise NotImplementedError

    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return self.__dict__ == value.__dict__
        if isinstance(value, DataFrame):
            return self._data_frame == value  # type: ignore
        if isinstance(value, list):
            return self._rows == value
        raise NotImplementedError

    @property
    def data_frame(self):
        data_frame = copy.deepcopy(self._data_frame)
        return data_frame

    @property
    def rows(self):
        rows = copy.deepcopy(self._rows)
        return rows

    def dump(self) -> None:
        """
        データのダンプ
        """
        print("---------- dump ----------")
        print(f"rows: {len(self._rows)}")
        for i, row in enumerate(self._rows):
            print(f"{i} - {row}")

    def validate(self, tolerate_nan: bool = False) -> None:
        """
        データのバリデーション

        Parameters:
        tolerate_nan (bool): 欠損値を許容するかのフラグ
        """
        print("---------- validate ----------")
        print(f"rows: {len(self._rows)}")
        for i, row in enumerate(self._rows):
            for column, value in row.items():
                if isinstance(value, str):
                    continue
                if tolerate_nan and math.isnan(value):
                    continue
                print(f"row: {i} - column: {column} - value: {value}")


#
# MTPPFile クラス
#


class MTPPFile:
    """
    ファイルからの読み込みと書き込みを行う基底クラス
    """


#
# MTPPCall クラス
#


class MTPPCall:
    """
    何らかの処理をするためのクラス

    実際の処理はクロージャ(関数，メソッド，ラムダ関数)をつくりそれを__call__メソッドに渡すことで行う
    """
