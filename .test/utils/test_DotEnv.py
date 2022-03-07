"""
 * @file   : test_DotEnv.py
 * @time   : 8:36
 * @date   : 2022/1/6
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os
import dotenv

from hilandBasicLibrary.io.pathHelper import PathHelper
from hilandBasicLibrary.projectHelper import ProjectHelper


def test_load_type():
    """
    测试两种加载方式
    :return:
    """

    root = ProjectHelper.get_root_physical_path()
    env_path = PathHelper.combine(root, '.env')

    # -- 加载方式1 ------------------------------
    dotenv.load_dotenv(env_path)
    actual = os.getenv("db_mongodb.port")
    expected = '27017'
    assert actual == expected

    # -- 加载方式2 ------------------------------
    actual = dotenv.get_key(env_path, "db_mysql.table_prefix")
    expected = "tmp_"
    assert actual == expected

    # -- 加载方式3 ------------------------------
    dot_dict = dotenv.dotenv_values(env_path)
    actual = dot_dict["db_mongodb.database"]
    expected = "stocks"
    assert actual == expected
