import pandas

from .core import MTPPData


#
# ヘルパー関数
#


def merge_data(data1: MTPPData, data2: MTPPData, *args, **kwargs) -> MTPPData:
    """
    2つのMTPPDataの表をマージ

    Parameters:
    data1 (MTPPData): 1つめのデータ
    data2 (MTPPData): 2つめのデータ
    """
    data_frame = pandas.merge(data1.data_frame, data2.data_frame, *args, **kwargs)

    return MTPPData(data_frame)


def select_column(data: MTPPData, columns: list[str]) -> MTPPData:
    """
    カラムを選択して返す

    Parameters:
    data (MTPPData): データ
    columns (list[str]): 選択するカラムのリスト
    """
    data_frame = data.data_frame[columns]

    return MTPPData(data_frame)
