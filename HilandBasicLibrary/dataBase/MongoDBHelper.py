"""本模块内均为单独执行的方法，具体针对collection的时候请使用MongoOperator内的类型"""
import pymongo
from builtins import *

from hiland.ConfigHelper import *


def get_current_db(database_name='', host='', port=0):
    if host == '':
        host = get_config_item("db_mongodb", "host")

    if port == 0:
        port = get_config_item("db_mongodb", "port")
        if port is None:
            port = 27017
        port = int(port)

    if database_name == '':
        database_name = get_config_item("db_mongodb", "database")

    _client = pymongo.MongoClient(host, port)
    _myDB = _client[database_name]

    return _myDB


def get_using_collection(collection_name, dbname='', host='', port=0):
    return get_current_db(dbname, host, port)[collection_name]


def insert_one(collection, data):
    """直接使用insert() 可以插入一条和插入多条 不推荐 明确区分比较好"""
    res = collection.insert_one(data)
    return res.inserted_id


def insert_many(collection, data_list):
    res = collection.insert_many(data_list)
    return res.inserted_ids


def find_one(collection, data, data_field={}):
    if len(data_field):
        res = collection.find_one(data, data_field)
    else:
        res = collection.find_one(data)
    return res


def find_many(collection, data, data_field={}):
    """ data_field 是指输出 操作者需要的字段"""
    if len(data_field):
        res = collection.find(data, data_field)
    else:
        res = collection.find(data)
    return res


def update_one(collection, data_condition, data_set):
    """修改一条数据"""
    res = collection.update_one(data_condition, data_set)
    return res


def update_many(collection, data_condition, data_set):
    """ 修改多条数据 """
    res = collection.update_many(data_condition, data_set)
    return res


def replace_one(collection, data_condition, data_set):
    """ 完全替换掉 这一条数据， 只是 _id 不变"""
    res = collection.replace_one(data_condition, data_set)
    return res


def delete_many(collection, data):
    res = collection.delete_many(data)
    return res


def delete_one(collection, data):
    res = collection.delete_one(data)
    return res



