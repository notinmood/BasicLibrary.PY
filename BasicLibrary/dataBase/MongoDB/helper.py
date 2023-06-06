"""本模块内均为单独执行的方法，具体针对 collection 的时候请使用 MongoOperator内的类型"""
import pymongo

from BasicLibrary.configHelper import ConfigHelper


class Helper:
    """

        """

    @classmethod
    def get_current_db(cls, database_name='', host='', port=0):
        if host == '':
            host = ConfigHelper.get_item("db_mongodb", "host")

        if port == 0:
            port = ConfigHelper.get_item("db_mongodb", "port", 27017)
            port = int(port)

        if database_name == '':
            database_name = ConfigHelper.get_item("db_mongodb", "database")

        _client = pymongo.MongoClient(host, port)
        _currentDB = _client[database_name]

        return _currentDB

    @classmethod
    def get_using_collection(cls, collection_name, dbname='', host='', port=0):
        return cls.get_current_db(dbname, host, port)[collection_name]

    @classmethod
    def insert_one(cls, collection, data):
        """
        虽然直接使用insert() 可以插入一条和插入多条 ,
        但还是推荐使用本方法，明确区分插入一条还是多条
        :param collection:
        :param data:
        :return:
        """
        res = collection.insert_one(data)
        return res.inserted_id

    @classmethod
    def insert_many(cls, collection, data_list):
        res = collection.insert_many(data_list)
        return res.inserted_ids

    @classmethod
    def find_one(cls, collection, data, data_field={}):
        if len(data_field):
            res = collection.find_one(data, data_field)
        else:
            res = collection.find_one(data)
        return res

    @classmethod
    def find_many(cls, collection, data, data_field={}):
        """ data_field 是指输出 操作者需要的字段"""
        if len(data_field):
            res = collection.find(data, data_field)
        else:
            res = collection.find(data)
        return res

    @classmethod
    def update_one(cls, collection, data_condition, data_set):
        """修改一条数据"""
        res = collection.update_one(data_condition, data_set)
        return res

    @classmethod
    def update_many(cls, collection, data_condition, data_set):
        """ 修改多条数据 """
        res = collection.update_many(data_condition, data_set)
        return res

    @classmethod
    def replace_one(cls, collection, data_condition, data_set):
        """ 完全替换掉 这一条数据， 只是 _id 不变"""
        res = collection.replace_one(data_condition, data_set)
        return res

    @classmethod
    def delete_many(cls, collection, data):
        res = collection.delete_many(data)
        return res

    @classmethod
    def delete_one(cls, collection, data):
        res = collection.delete_one(data)
        return res
