import pandas
from typing import Literal, Optional, Union
from pandas import DataFrame, Series
from .core import MTPPCall, MTPPData


#
# MTPPPandas クラス
#


class MTPPPandas(MTPPCall):
    """
    Pandasで処理をするためのクラス

    実際の処理はクロージャ(関数，メソッド，ラムダ関数)をつくりそれを__call__メソッドに渡すことで行う
    """

    def __call__(self, data: MTPPData, call_function, /, *args) -> MTPPData:
        """
        Pandasで処理をするメソッド

        Parameters:
        call_function (クロージャ): 実際に処理を行うクロージャ
        data (MTPPData): 処理のためのデータ
        """
        if not isinstance(data, MTPPData):
            raise TypeError

        data_frame = data.data_frame

        if isinstance(call_function, list):
            for function in call_function:
                if isinstance(function, tuple):
                    function, *args = function  # type: ignore
                    data_frame = function(data_frame, *args)
                else:
                    data_frame = function(data_frame)
        else:
            data_frame = call_function(data_frame, *args)

        return MTPPData(data_frame)


#
# ヘルパー関数
#


def reset_index(data_frame: DataFrame) -> DataFrame:
    return data_frame.reset_index()


def merge_data_frame(data_frame1: DataFrame, data_frame2: DataFrame, /, *args, **kwargs) -> DataFrame:
    return pandas.merge(data_frame1, data_frame2, *args, **kwargs)


def select_row(data_frame: DataFrame, row: Series) -> DataFrame:
    return data_frame[row]


def select_column(data_frame: DataFrame, columns: list[str]) -> DataFrame:
    return data_frame[columns]


def rename_column(data_frame: DataFrame, column_from: str, column_to: str) -> DataFrame:
    return data_frame.rename(columns={column_from: column_to})


def sort_values(data_frame: DataFrame, by: list[str]) -> DataFrame:
    return data_frame.sort_values(by)


def sum_of_column(
    data_frame: DataFrame, column: str, /, groupby: Optional[list[str]] = None, as_index: bool = True
) -> Union[DataFrame, Series]:
    if groupby is None:
        return data_frame[column].sum()
    return data_frame.groupby(groupby, as_index=as_index)[column].sum()


def cumsum_of_column(data_frame: DataFrame, column: str, /, groupby: Optional[list[str]] = None) -> Series:
    if groupby is None:
        return data_frame[column].cumsum()
    return data_frame.groupby(groupby)[column].cumsum()


def rank_of_column(
    data_frame: DataFrame,
    column: str,
    /,
    groupby: Optional[list[str]],
    method: Literal["average", "min", "max", "first", "dense"],
    ascending: bool = True,
) -> Series:
    if groupby is None:
        return data_frame[column].rank(method=method, ascending=ascending).astype(int)
    return data_frame.groupby(groupby)[column].rank(method=method, ascending=ascending).astype(int)


def value_to_missing_value(series: Series, value: str) -> Series:
    return series.replace(value, None)


def empty_to_missing_value(series: Series) -> Series:
    return value_to_missing_value(series, "")


def missing_value_to_value(series: Series, value: str) -> Series:
    return series.fillna(value)


def missing_value_to_empty(series: Series) -> Series:
    return missing_value_to_value(series, "")
