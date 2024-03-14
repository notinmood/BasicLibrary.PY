"""
 * @file   : test_ImageHelper.py
 * @time   : 7:51
 * @date   : 2024/3/14
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path

from BasicLibrary.io.imageHelper import ImageHelper
from BasicLibrary.projectHelper import ProjectHelper


def test_get_size():
    root_path = ProjectHelper.get_root_physical_path()
    file_full_name = os.path.join(root_path, r".test/_res/images/testjpg.jpg")
    actual = ImageHelper.get_size(file_full_name)
    expected = (1242, 1660)
    assert actual == expected

    file_full_name = os.path.join(root_path, r".test/_res/images/testpng.png")
    actual = ImageHelper.get_size(file_full_name)
    expected = (1080, 810)
    assert actual == expected

    file_full_name = os.path.join(root_path, r".test/_res/images/testwebp.webp")
    actual = ImageHelper.get_size(file_full_name)
    expected = (1200, 1599)
    assert actual == expected


def test_get_format():
    root_path = ProjectHelper.get_root_physical_path()

    file_full_name = os.path.join(root_path, r".test/_res/images/testjpg.jpg")
    actual = ImageHelper.get_format(file_full_name)
    expected = "jpeg"
    assert actual == expected

    file_full_name = os.path.join(root_path, r".test/_res/images/testpng.png")
    actual = ImageHelper.get_format(file_full_name)
    expected = "png"
    assert actual == expected

    file_full_name = os.path.join(root_path, r".test/_res/images/testwebp.webp")
    actual = ImageHelper.get_format(file_full_name)
    expected = "webp"
    assert actual == expected

    file_full_name = os.path.join(root_path, r".test/_res/images/testtxt.txt")
    actual = ImageHelper.get_format(file_full_name)
    expected = None
    assert actual == expected
