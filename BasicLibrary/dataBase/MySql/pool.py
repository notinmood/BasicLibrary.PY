import pymysql
from dbutils.pooled_db import PooledDB

from BasicLibrary.configHelper import ConfigHelper as ch


class _PoolConfig(object):
    """

    """

    def __init__(self):
        self.host = ch.get_item("db_mysql", "host")
        self.port = int(ch.get_item("db_mysql", "port", 3306))
        self.db = ch.get_item("db_mysql", "database")
        self.user = ch.get_item("db_mysql", "user", "root")
        self.password = ch.get_item("db_mysql", "password", "")
        self.charset = ch.get_item("db_mysql", "charset", "utf8")

        # creator：数据库驱动模块，如常见的pymysql,pymssql,cx_Oracle模块。无默认值
        # mincached：初始化连接池时创建的连接数。默认为0，即初始化时不创建连接。(建议默认0，假如非0的话，在某些数据库不可用时，整个项目会启动不了)
        # maxcached：池中空闲连接的最大数量。默认为0，即无最大数量限制。(建议默认)
        # maxshared：池中共享连接的最大数量。默认为0，即每个连接都是专用的，不可共享(不常用，建议默认)
        # maxconnections：被允许的最大连接数。默认为0，无最大数量限制。(视情况而定)
        # blocking：连接数达到最大时，新连接是否可阻塞。默认False，即达到最大连接数时，再取新连接将会报错。(建议True，达到最大连接数时，新连接阻塞，等待连接数减少再连接)
        # maxusage：连接的最大使用次数。默认0，即无使用次数限制。(建议默认)
        # setsession：可选的SQL命令列表，可用于准备会话。(例如设置时区)
        # reset：当连接放回连接池时，是否每次都调用 rollback 以保证事务终止，为 False 或 None 则不额外调用 rollback 方法
        # ————————————————
        # 版权声明：本文为CSDN博主「shawn_wxn」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
        # 原文链接：https://blog.csdn.net/diuleilaomu/article/details/103278147
        self.minCached = 0
        self.maxCached = 0
        self.maxShared = 0
        self.maxUsage = 0
        self.maxConnection = int(ch.get_item("project_data", "database_connection_pool_count", 10))

        self.blocking = True
        self.setSession = None
        self.reset = True


class Pool(object):
    def __init__(self):
        config = _PoolConfig()

        self.__pool = PooledDB(creator=pymysql,
                               maxconnections=config.maxConnection,
                               mincached=config.minCached,
                               maxcached=config.maxCached,
                               maxshared=config.maxShared,
                               blocking=config.blocking,
                               maxusage=config.maxUsage,
                               setsession=config.setSession,
                               charset=config.charset,
                               host=config.host,
                               port=config.port,
                               database=config.db,
                               user=config.user,
                               password=config.password,
                               )

    def get_conn(self):
        return self.__pool.connection()
