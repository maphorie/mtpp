from pandas import DataFrame
from mtpp import MTPPData, MTPPPandas
from .constant import (
    PANDAS_BEFORE_CALL,
    PANDAS_AFTER_CALL,
)


def pandas_call_function(data_frame: DataFrame) -> DataFrame:
    # 前処理
    data_frame["カラム1"] = data_frame["カラム1"].astype(int)
    data_frame["カラム2"] = data_frame["カラム2"].astype(int)

    # 本処理
    data_frame["カラム比"] = data_frame["カラム1"] / data_frame["カラム2"]

    # 後処理
    data_frame["カラム1"] = data_frame["カラム1"].astype(str)
    data_frame["カラム2"] = data_frame["カラム2"].astype(str)
    data_frame["カラム比"] = data_frame["カラム比"].astype(str)

    return data_frame


class TestMTPPPandas:
    def test_instance(self):
        target = MTPPPandas()
        assert isinstance(target, MTPPPandas)

    def test_call(self):
        target = MTPPPandas()
        before = MTPPData(PANDAS_BEFORE_CALL)
        after = target(before, pandas_call_function)
        assert after == PANDAS_AFTER_CALL
