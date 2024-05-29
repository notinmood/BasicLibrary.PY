"""
 * @file   : test_StringHelper.py
 * @time   : 21:57
 * @date   : 2021/11/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.stringHelper import StringHelper


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

    expected = True
    actual = StringHelper.is_contains("qingdao", ("dao", "qi"))
    assert actual == expected


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

    # +--------------------------------------------------------------------------
    # |::::TIPS::::| 本代码的使用说明
    # ---------------------------------------------------------------------------
    # 因为集合内的元素是无序的，所以通过implode得到字符串不是确定
    # 我们断言的时候，只能判断某个元素是否存在拼接后的字符串内
    # +--------------------------------------------------------------------------
    actual = StringHelper.implode(_data)
    assert actual.index("qingdao") >= 0
    assert actual.index("beijing") >= 0
    assert actual.index("shanghai") >= 0


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


def test_insert_fixer():
    whole = "hello,china"
    actual = StringHelper.insert_fixer(whole, "w", "-")
    expected = "hello,china"
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.insert_fixer(whole, ",", "-")
    expected = "hello-,china"
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.insert_fixer(whole, ",", "-", False)
    expected = "hello,-china"
    assert actual == expected


def test_get_length():
    whole = "I love 中国"
    actual = StringHelper.get_length(whole)
    expected = 9
    assert actual == expected


def test_add_padding():
    whole = "qingdao"
    actual = StringHelper.add_padding(whole, 5)
    expected = "qingdao"
    assert actual == expected

    whole = "qingdao"
    actual = StringHelper.add_padding(whole, 10)
    expected = "000qingdao"
    assert actual == expected

    whole = "qingdao"
    actual = StringHelper.add_padding(whole, 10, "-", False)
    expected = "qingdao---"
    assert actual == expected


def test_explode1():
    whole = "hello,china,boy"
    actual = StringHelper.explode(whole, ",")
    expected = ["hello", "china", 'boy']
    assert actual == expected

    whole = "hello,china"
    actual = StringHelper.explode(whole, ".")
    expected = ["hello,china"]
    assert actual == expected


def test_explode2():
    whole = "hello,china.boy"
    actual = StringHelper.explode(whole, [",", "."])
    expected = ['hello', 'china', 'boy']
    assert actual == expected


def test_explode3():
    whole = "hello,china.boy;"
    actual = StringHelper.explode(whole, [",", ".", ";"])
    expected = ['hello', 'china', 'boy', '']
    expected = expected
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


def test_replace():
    whole = 'C:\\Users\\Administrator\\Downloads\\app_26822737\\db0e400fad35ba8e18ac06bd9bd99f2752.jpeg'
    old = r'C:\\Users\\Administrator\\Downloads\\app_26822737'
    new = r'E:\\MyImages\\美女图片未整理\\app_26822737'
    actual = StringHelper.replace(whole, old, new)
    expected = "E:\\MyImages\\美女图片未整理\\app_26822737\\db0e400fad35ba8e18ac06bd9bd99f2752.jpeg"
    assert actual == expected


pass


def test_replace2():
    whole = r'C:\Users\Administrator\db0e400fad35ba8e18ac06bd9bd99f2752.jpeg'
    old = r'C:\Users\Administrator'
    new = r'E:\MyImages\美女图片未整理\app_26822737'
    actual = StringHelper.replace(whole, old, new, False)
    expected = r"E:\MyImages\美女图片未整理\app_26822737\db0e400fad35ba8e18ac06bd9bd99f2752.jpeg"
    assert actual == expected


def test_replace3():
    text = '今天是：11/28/2018'
    actual = StringHelper.replace(text, r"(\d{2})/(\d{2})/(\d{4})", r"\3年\1月\2日")
    expected = '今天是：2018年11月28日'
    assert actual == expected


pass


def test_replace4():
    text = '-->_1_金句摘抄｜关于奋斗_1.png.ocr.txt<--'
    actual = StringHelper.replace(text, r"-->(.*).ocr.txt<--", r"[\1](\1)")
    expected = '[_1_金句摘抄｜关于奋斗_1.png](_1_金句摘抄｜关于奋斗_1.png)'
    assert actual == expected


pass


def test_sub_string1():
    whole = "男人为什么不能嫖娼？ 人生道路上，有许多迷雾难以剖析。"
    start = 1
    length = 1
    actual = StringHelper.sub_string(whole, start, length)
    expected = "人"
    assert actual == expected


pass


def test_sub_string2():
    whole = "男人为什么不能嫖娼？ 人生道路上，有许多迷雾难以剖析。"
    start = 1
    length = 9
    actual = StringHelper.sub_string(whole, start, length)
    expected = "人为什么不能嫖娼？"
    assert actual == expected


pass


def test_sub_string3():
    whole = "男人为什么不能PC?!人生道路上，有许多迷雾难以剖析。"
    start = 1
    length = 9
    actual = StringHelper.sub_string(whole, start, length)
    expected = "人为什么不能PC?"
    assert actual == expected


pass


def test_sub_string4():
    whole = "男人为什么不能PC??"
    start = 1
    length = 20
    actual = StringHelper.sub_string(whole, start, length)
    expected = "人为什么不能PC??"
    assert actual == expected


pass


def test_sub_string5():
    whole = "男人为什么不能PC?!人生道路上，有许多迷雾难以剖析。"
    start = -1
    length = 2
    actual = StringHelper.sub_string(whole, start, length)
    expected = "剖析"
    assert actual == expected


pass


def test_happy_path():
    result = StringHelper.split_with_keeping_delimiter("abc.def.ghi", ".")
    assert result == ['abc.', 'def.', 'ghi']


def test_edge_case_empty_string():
    result = StringHelper.split_with_keeping_delimiter("", ".")
    assert result == ['']


def test_edge_case_null_string():
    result = StringHelper.split_with_keeping_delimiter(None, ".")
    assert result == ['']


def test_edge_case_no_delimiter():
    result = StringHelper.split_with_keeping_delimiter("abcde", ".")
    assert result == ['abcde']


def test_edge_case_multiple_delimiters():
    result = StringHelper.split_with_keeping_delimiter("a.b.c.d", ".")
    assert result == ['a.', 'b.', 'c.', 'd']


def test_edge_case_multiple_delimiters2():
    result = StringHelper.split_with_keeping_delimiter("a.b.c.d.", ".")
    assert result == ['a.', 'b.', 'c.', 'd.']
