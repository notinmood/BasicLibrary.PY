"""
 * @file   : test_pandasHelper.py
 * @time   : 16:40
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import pandas as pd
import pytest

from BasicLibrary.data.pandasHelper import PandasHelper


@pytest.fixture
def gen_data():
    a = [0, 1, 2, 3, 4]
    b = [1, 4, 5]
    pd_a = pd.DataFrame(a)
    pd_b = pd.DataFrame(b)
    return pd_a, pd_b


def test_get_difference_single(gen_data):
    pd_a, pd_b = gen_data
    pd_s = PandasHelper.get_difference_single(pd_a, pd_b)

    item0 = pd_s[0]
    actual = len(item0)
    expected = 3
    assert actual == expected

    pd_s = PandasHelper.get_difference_single(pd_b, pd_a)
    item0 = pd_s[0]
    actual = len(item0)
    expected = 1
    assert actual == expected


def test_get_union(gen_data):
    pd_a, pd_b = gen_data
    pd_s = PandasHelper.get_union(pd_a, pd_b)
    item0 = pd_s[0]
    actual = len(item0)
    expected = 6
    assert actual == expected


def test_get_intersection(gen_data):
    pd_a, pd_b = gen_data
    pd_s = PandasHelper.get_intersection(pd_a, pd_b)
    item0 = pd_s[0]
    actual = len(item0)
    expected = 2
    assert actual == expected
