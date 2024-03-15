import pandas as pd


class PandasHelper:
    """
    Pandas Helper
    """

    @staticmethod
    def is_exist_column(dataframe, column_name):
        if column_name in dataframe.columns:
            return True
        else:
            return False
        pass

    pass

    @staticmethod
    def is_empty(dataframe):
        return dataframe.empty

    pass

    @staticmethod
    def get_column_count(dataframe):
        return dataframe.columns.size

    pass

    @staticmethod
    def get_row_count(dataframe):
        return len(dataframe)

    pass

    @staticmethod
    def get_column_names(dataframe):
        """
        获取dataframe的列名称list
        :param dataframe:
        :return:
        """
        return dataframe.columns.tolist()

    pass

    @staticmethod
    def get_element(dataframe, row_info, column_info):
        """
        获取dataframe中的某一个元素
        :param dataframe: 目标dataframe
        :param row_info: 如果是数字就表示行索引号（即缺省索引），如果是字符串就表示行索引字符（通常为自定义索引）
        :param column_info: 如果是数字就表示列的索引号，如果是字符串就表示列名称
        :return:
        """
        if type(row_info) is int:
            row = dataframe.iloc[row_info]
        else:
            row = dataframe.loc[row_info]
        pass

        if type(column_info) is int:
            return row.iat[column_info]
        else:
            return row.at[column_info]
        pass

    pass

    @staticmethod
    def convert_cursor_to_dataframe(cursor):
        return pd.DataFrame(list(cursor))

    pass

    @staticmethod
    def loop_data_frame(data, func4item, *args, **kwargs):
        """
        这是一个循环处理pandas中DataFrame的每一条记录的方法
        :param data: 待处理的DataFrame
        :param func4item: 处理DataFrame每条记录的方法，这个方法的参数为(item, result_4_loops)，
        其中item表示DataFrame的一行记录（在读取item的字段的时候，使用如下格式 item['name']），
        其中result_4_loops表示在穿越于整个loops各个循环间的数据，循环结束并返回这个信息,這個值通常用dict类型表示
        :return:
        """
        result_4_loops = None
        for my_index, my_item in data.iterrows():
            result_4_loops = func4item(my_item, result_4_loops, *args, **kwargs)
        pass

        return result_4_loops

    pass

    @staticmethod
    def get_union(df_a, df_b):
        # 取合集：df1和df2所有数据的集合
        union_result = pd.merge(df_a, df_b, how='outer')
        return union_result

    pass

    @staticmethod
    def get_intersection(df_a, df_b):
        # 取交集：既在df1中，也在df2中
        intersection_result = pd.merge(df_a, df_b)
        return intersection_result

    pass

    @staticmethod
    def get_difference(df_a, df_b):
        """
        求a对b的差集
        :param df_a:
        :param df_b:
        :return:
        """
        diff = pd.concat([df_a, df_b, df_b]).drop_duplicates(keep=False)
        return diff

    pass

    # TODO:xiedali@2024/03/15 求双向差集


pass
