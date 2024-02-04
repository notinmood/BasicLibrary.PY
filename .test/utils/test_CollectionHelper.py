"""
 * @file   : test_CollectionHelper.py
 * @time   : 16:18
 * @date   : 2021/12/4
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.collectionHelper import *


def test_is_contains_1():
    my_list = [7, 1, 9, 5, 3]
    actual = CollectionHelper.is_contains(my_list, 5)
    expected = True
    assert actual == expected


def test_is_contains_2():
    my_list = [7, 1, 9, 5, 3]
    actual = CollectionHelper.is_contains(my_list, 6)
    expected = False
    assert actual == expected


def test_is_contains_3():
    my_list = (7, 1, 9, 5, 3)
    actual = CollectionHelper.is_contains(my_list, 5)
    expected = True
    assert actual == expected


def test_is_contains_4():
    my_list = (7, 1, 9, 5, 3)
    actual = CollectionHelper.is_contains(my_list, 6)
    expected = False
    assert actual == expected


def test_is_contains_5():
    data = {"name": "zhangsan", "age": 20, "score": 93}
    actual = CollectionHelper.is_contains(data, "name", "zhangsan")
    expected = True
    assert actual == expected

    actual = CollectionHelper.is_contains(data, "name", "lisi")
    expected = False
    assert actual == expected

    actual = CollectionHelper.is_contains(data, "school", "")
    expected = False
    assert actual == expected


def test_sort_1():
    """
    测试对 list 排序
    :return:
    """
    my_list = [7, 1, 9, 5, 3]
    actual = CollectionHelper.sort(my_list)
    expected = [1, 3, 5, 7, 9]
    assert actual == expected


def test_sort_for_inner_dict():
    my_list = [{"name": "zhangsan", "age": 20, "score": 93},
               {"name": "lisi", "age": 19, "score": 94},
               {"name": "wangwu", "age": 21, "score": 92}]
    actual = CollectionHelper.sort_dict(my_list, "age")
    expected = [{'name': 'lisi', 'age': 19, 'score': 94},
                {'name': 'zhangsan', 'age': 20, 'score': 93},
                {'name': 'wangwu', 'age': 21, 'score': 92}]
    assert actual == expected

    actual = CollectionHelper.sort_dict(my_list, "score")
    expected = [{'name': 'wangwu', 'age': 21, 'score': 92},
                {'name': 'zhangsan', 'age': 20, 'score': 93},
                {'name': 'lisi', 'age': 19, 'score': 94}]
    assert actual == expected


def test_sort():
    s = "德国 10 11 16\n意大利 10 10 20\n荷兰 10 12 14\n法国 10 12 11\n英国 22 21 22\n中国 38 32 18\n日本 27 14 17\n美国 39 41 33\n俄罗斯奥委会 20 28 23\n澳大利亚 17 7 22\n匈牙利 6 7 7\n加拿大 7 6 11\n古巴 7 3 5\n巴西 7 6 8\n新西兰 7 6 7"
    stodata = s.split('\n')
    # print(stodata)

    # 使用sorted
    para = {}

    for line in range(len(stodata)):
        # 每一行数据
        data = stodata[line].split(' ')
        # print(data)
        # 组装数据结构para={'China': [], 'Russia': []}
        para[data[0]] = [int('-' + i) for i in data[1:]]

    # # 开始排序(x[1]代表奖牌数目, x[0]代表国家)
    # new_para = sorted(para.items(), key=lambda x: (x[1], x[0]))
    # # print(para)
    # print("────────────────────────")
    # print(para.items())
    # print('────────────────────────')
    # print(new_para)
    #
    # c = []
    # for i in new_para:
    #     c.append((i[0]))
    # for j in range(len(c)):
    #     print(f"{(j + 1):2d}  {c[j]}")

    new_sorted = CollectionHelper.sort(para.items(), key=lambda x: (x[1], x[0]), reverse=False)
    print(new_sorted)
