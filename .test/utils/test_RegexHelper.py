"""
 * @file   : test_RegexHelper.py
 * @time   : 18:21
 * @date   : 2022/3/17
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.regexHelper import RegexHelper


def test_get_matched_items():
    whole = "I am in Tengzhou(0632),and I love Qingdao(0532)!"
    pattern = r"\d+"

    actual = RegexHelper.get_matched_items(whole, pattern)
    expected = ['0632', '0532']
    assert actual == expected

    pattern = r"^\d+"
    actual = RegexHelper.get_matched_items(whole, pattern)
    expected = []
    assert actual == expected


def test_determine_is_matched():
    whole = "I am in Tengzhou(0632),and I love Qingdao(0532)!"
    pattern = r"^\d+"
    actual = RegexHelper.determine_is_matched(whole, pattern)
    expected = False
    assert actual == expected


def test_replace():
    text = '今天是：11/28/2018'
    actual = RegexHelper.replace(text, r"(\d{2})/(\d{2})/(\d{4})", r"\3年\1月\2日")
    expected = '今天是：2018年11月28日'
    assert actual == expected
