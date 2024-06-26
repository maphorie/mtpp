import pandas

from .core import MTPPData


#
# ヘルパー関数
#


def merge_data(left: MTPPData, right: MTPPData, *args, **kwargs) -> MTPPData:
    """
    2つのMTPPDataをマージ

    Parameters:
    left (MTPPData): 1つめのデータ
    right (MTPPData): 2つめのデータ
    """
    data_frame = pandas.merge(left.data_frame, right.data_frame, *args, **kwargs)

    return MTPPData(data_frame)


def concat_data(data_list: list[MTPPData], *args, **kwargs) -> MTPPData:
    """
    2つ以上のMTPPDataを結合

    Parameters:
    data_list (list[MTPPData]): データのリスト
    """
    data_frame_list = [data.data_frame for data in data_list]

    data_frame = pandas.concat(data_frame_list, *args, **kwargs)

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
