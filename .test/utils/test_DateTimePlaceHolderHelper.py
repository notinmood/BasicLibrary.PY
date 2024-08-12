"""
 * @file   : test_DateTimePlaceHolderHelper.py
 * @time   : 下午8:31
 * @date   : 2024/8/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.dateTimePlaceHolderHelper import DateTimePlaceHolderHelper


def test_get_full_biz_strings():
    biz_string_with_placeholder = "z:/x/{yyyymm}/y/{yyyymmdd}/z"
    actual = DateTimePlaceHolderHelper.get_full_biz_strings(biz_string_with_placeholder, '20240830', '20240902')
    expected = ['z:/x/202408/y/20240830/z',
                'z:/x/202408/y/20240831/z',
                'z:/x/202409/y/20240901/z',
                'z:/x/202409/y/20240902/z']

    assert actual == expected


pass
