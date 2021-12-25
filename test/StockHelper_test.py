"""
 * @file   : StockHelper_test.py
 * @time   : 17:02
 * @date   : 2021/11/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.biz.StockHelper import StockHelper as sh


def test_get_stock_exchange_name():
    biz_data = "600690"
    actual = sh.get_stock_exchange_name(biz_data)
    expected = "SH"
    assert actual == expected

    biz_data = "600690.SH"
    actual = sh.get_stock_exchange_name(biz_data)
    expected = "SH"
    assert actual == expected

    biz_data = "sh.600690"
    actual = sh.get_stock_exchange_name(biz_data)
    expected = "SH"
    assert actual == expected

    biz_data = "300690"
    actual = sh.get_stock_exchange_name(biz_data)
    expected = "SZ"
    assert actual == expected


def test_get_standard_code():
    biz_data = "600690"
    actual = sh.get_standard_code(biz_data)
    expected = "600690"
    assert actual == expected

    biz_data = "这是海尔的股票代码600690,2021年最高价格为38元。"
    actual = sh.get_standard_code(biz_data)
    expected = "600690"
    assert actual == expected

    biz_data = "这不是一个股票代码500690"
    actual = sh.get_standard_code(biz_data)
    expected = ""
    assert actual == expected

    biz_data = "股市在2045点"
    actual = sh.get_standard_code(biz_data)
    expected = ""
    assert actual == expected


def test_format_stock_code():
    biz_data = "600690"
    actual = sh.format_stock_code(biz_data)
    expected = "SH600690"
    assert actual == expected

    biz_data = "600690"
    actual = sh.format_stock_code(biz_data, "", ".[sen]")
    expected = "600690.sh"
    assert actual == expected

    biz_data = "600690"
    actual = sh.format_stock_code(biz_data, "cn-", ".[Sen]")
    expected = "cn-600690.SH"
    assert actual == expected
