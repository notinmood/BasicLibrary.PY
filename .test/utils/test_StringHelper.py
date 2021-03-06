"""
 * @file   : test_StringHelper.py
 * @time   : 21:57
 * @date   : 2021/11/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.stringHelper import *


def test_reverse():
    original = "123456789"
    actual = StringHelper.reverse(original)
    expected = "987654321"
    assert actual == expected


def test_is_contains():
    expected = True
    actual = StringHelper.is_contains("qingdao", "dao")
    assert actual == expected

    expected = True
    actual = StringHelper.is_contains("beijing", "dao")
    assert actual != expected


def test_format():
    expected = "张三你好，欢迎来到中国。"
    actual = StringHelper.format("{0}你好，欢迎来到{1}。", "张三", "中国")
    assert actual == expected


def test_implode1():
    """
    对集合的操作
    :return:
    """
    _data = {'qingdao', 'beijing', 'shanghai'}

    """
    因为集合内的元素是无序的，所以通过implode得到字符串不是确定
    我们断言的时候，只能判断某个元素是否存在拼接后的字符串内
    """
    actual = StringHelper.implode(_data)
    assert actual.__contains__("qingdao")
    assert actual.__contains__("beijing")
    assert actual.__contains__("shanghai")


def test_implode2():
    """
    对列表的操作
    :return:
    """
    _data = ['qingdao', 'beijing', 'shanghai']
    actual = StringHelper.implode(_data)
    expected = "qingdao,beijing,shanghai"
    assert actual == expected


def test_remove_head():
    whole = "hello,china"
    actual = StringHelper.remove_head(whole, "hex")
    expected = whole
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.remove_head(whole, "hel")
    expected = "lo,china"
    assert actual == expected


def test_remove_tail():
    whole = "hello,china"
    actual = StringHelper.remove_tail(whole, "bna")
    expected = "hello,china"
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.remove_tail(whole, "ina")
    expected = "hello,ch"
    assert actual == expected


def test_get_before_content():
    whole = "hello,china"
    actual = StringHelper.get_before_content(whole, ".")
    expected = "hello,china"
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.get_before_content(whole, "h")
    expected = ""
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.get_before_content(whole, "llo")
    expected = "he"
    assert actual == expected


def test_get_after_content():
    whole = "hello,china"
    actual = StringHelper.get_after_content(whole, ".")
    expected = "hello,china"
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.get_after_content(whole, ",")
    expected = "china"
    assert actual == expected


def test_add_padding():
    whole = "hello,china"
    actual = StringHelper.add_padding(whole, "w", "-")
    expected = "hello,china"
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.add_padding(whole, ",", "-")
    expected = "hello-,china"
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.add_padding(whole, ",", "-", False)
    expected = "hello,-china"
    assert actual == expected


def test_get_length():
    whole = "I love 中国"
    actual = StringHelper.get_length(whole)
    expected = 9
    assert actual == expected


def test_set_padding():
    whole = "qingdao"
    actual = StringHelper.set_padding(whole, 5)
    expected = "qingdao"
    assert actual == expected

    whole = "qingdao"
    actual = StringHelper.set_padding(whole, 10)
    expected = "000qingdao"
    assert actual == expected

    whole = "qingdao"
    actual = StringHelper.set_padding(whole, 10, "-", False)
    expected = "qingdao---"
    assert actual == expected


def test_explode():
    whole = "hello,china"
    actual = StringHelper.explode(whole, ",")
    expected = ["hello", "china"]
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.explode(whole, ".")
    expected = ["hello,china"]
    assert actual == expected


def test_upper_all_chars():
    biz_data = "I love China!我爱中国！"
    actual = StringHelper.upper_all_chars(biz_data)
    expected = "I LOVE CHINA!我爱中国！"
    assert actual == expected


def test_lower_all_chars():
    biz_data = "I love China!我爱中国！"
    actual = StringHelper.lower_all_chars(biz_data)
    expected = "i love china!我爱中国！"
    assert actual == expected


def test_upper_first_char():
    biz_data = "i love China!我爱中国！"
    actual = StringHelper.upper_first_char(biz_data)
    expected = "I love China!我爱中国！"
    assert actual == expected


def test_lower_first_char():
    biz_data = "I love China!我爱中国！"
    actual = StringHelper.lower_first_char(biz_data)
    expected = "i love China!我爱中国！"
    assert actual == expected


def test_upper_first_char_every_word():
    biz_data = "i love china!我爱中国！"
    actual = StringHelper.upper_first_char_every_word(biz_data)
    expected = "I Love China!我爱中国！"
    assert actual == expected
