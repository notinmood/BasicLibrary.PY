"""
 * @file   : hilandSheet.py
 * @time   : 20:45
 * @date   : 2021/11/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from BasicLibrary.office.excelMisc import _calc_cell_marker


class ExcelSheetMate:
    """
    Excel 工作表
    !!!特别注意，单列数据的写入用二维数组，但单列数据的读出为一维数组。
    """

    def __init__(self, sheet):
        """
        从 xlwings 提供的 sheet 创建本地 Sheet
        :param sheet: xlwings 提供的 sheet 类型实例
        """
        self.original_sheet = sheet
        self.cell = None
        self.range_selected = None
        self.style = []

    def get_column_count(self) -> int:
        """
        获取行数
        :return:
        """
        col_value = self.original_sheet.used_range.last_cell.column
        return col_value

    def get_row_count(self) -> int:
        """
        获取列数
        :return:
        """
        row_value = self.original_sheet.used_range.last_cell.row
        return row_value

    def read(self, range_marker=None):
        """
        获取指定区块内的数值(get方法的别名)
        :param range_marker:区块的标志信息，可以取值如下几种之一：
            1. "A1"  # 返回单个单元格内的值信息 '姓名'
            2. "A1:A2" # 返回一维数组 ['姓名', '张三']
            3. "A1:B2" # 返回二维数组 [['姓名', '年龄'], ['张三', 20.0]]
            4. None # 通過二维數組的方式返回全部數據
        :return:
        """
        return self.get(range_marker)

    def get(self, range_marker=None):
        """
        获取指定区块内的数值
        :param range_marker:区块的标志信息，可以取值如下几种之一：
            1. "A1"  # 返回单个单元格内的值信息 '姓名'
            2. "A1:A2" # 一维数组 ['姓名', '张三']
            3. "A1:B2" # 二维数组 [['姓名', '年龄'], ['张三', 20.0]]
            4. None # 通過二维數組的方式返回全部數據
        :return:
        """
        if range_marker is None:
            row_count = self.get_row_count()
            column_count = self.get_column_count()
            if row_count > 0:
                row_count = row_count - 1

            if column_count > 0:
                column_count = column_count - 1

            last_cell_marker = _calc_cell_marker("A1", row_count, column_count)
            range_marker = f"A1:{last_cell_marker}"

        value = self.original_sheet.range(range_marker).value
        return value

    def write(self, range_data, range_marker=None):
        """
        写入数据(set方法的别名)
        1. 严格模式：请必须匹配 range_marker 和 range_data 的格式相同，数据量相同。
        2. 推断模式：如果仅仅给 range_marker 指定一个开始位置，而在 range_data 内给定一个一维数组或者二维数组的区域，
            那么 xlwings 将会自动推断写入的位置。
        :param range_marker::区块的标志信息，可以取值如下几种之一：
            1. "A1"  # 设置单个单元格内的值信息 '姓名'
            2. "A1:A2" # 一维数组 ['姓名', '张三']
            3. "A1:B2" # 二维数组 [['姓名', '年龄'], ['张三', 20.0]]
            4. "A1" # 二维数组 [['姓名', '年龄'], ['张三', 20.0]] （自动启用推断模式）
        :param range_data:要写入的数据。!!!特别注意，单列数据的写入用二维数组，但单列数据的读出为一维数组。
        :return:
        """
        return self.set(range_data, range_marker)

    def set(self, range_data, range_marker=None):
        """
        写入数据
        1. 严格模式：请必须匹配 range_marker 和 range_data 的格式相同，数据量相同。
        2. 推断模式：如果仅仅给 range_marker 指定一个开始位置，而在 range_data 内给定一个一维数组或者二维数组的区域，
            那么 xlwings 将会自动推断写入的位置。
        :param range_marker::区块的标志信息，可以取值如下几种之一：
            1. "A1"  # 设置单个单元格内的值信息 '姓名'
            2. "A1:A2" # 一维数组 ['姓名', '张三']
            3. "A1:B2" # 二维数组 [['姓名', '年龄'], ['张三', 20.0]]
            4. "A1" # 二维数组 [['姓名', '年龄'], ['张三', 20.0]] （自动启用推断模式）
        :param range_data:要写入的数据。!!!特别注意，单列数据的写入用二维数组，但单列数据的读出为一维数组。
        :return:
        """
        if range_marker is None:
            range_marker = "A1"
        pass
        self.original_sheet.range(range_marker).value = range_data
        return

    def rename(self, sheet_new_name: str):
        """
        sheet重命名
        :param sheet_new_name:
        :return:
        """
        self.original_sheet.name = sheet_new_name

    def get_name(self):
        return self.original_sheet.name

    def copy(self, range_marker):
        """
        复制
        :param range_marker:
        :return:
        """
        self.range_selected = self.original_sheet.range(range_marker).value
        return self.range_selected

    def paste(self, range_marker, range_data=None):
        """
        粘贴
        :param range_marker:
        :param range_data:
        :return:
        """
        if not range_data:
            range_data = self.range_selected

        self.original_sheet.range(range_marker).value = range_data
        return

    # # # 复制
    # def copy(self, sheet_name, range_col_row):
    #     self.my_range = self.original_sheet.range(sheet_name, range_col_row).value
    #     return self.my_range
    #
    # # 粘贴
    # def paste(self, sheet_name, range_col_row):
    #     self.original_sheet.range(sheet_name, range_col_row).value = self.my_range
    #     return
    #
    # # 粘贴数据
    # def paste_range(self, sheet_name, range_col_row):
    #     self.original_sheet.range(sheet_name, range_col_row).value = self.my_range
    #     return

    # # 排序
    # def sort(self, cell_pos):
    #     self.original_sheet.range(cell_pos).api.Sort(Key1=self.original_sheet.range(cell_pos).api, Order1=1)
    #     return
    #
    # # 过滤条件
    # def filter(self, col, data):
    #     # filter_data = self.sheet.range.filter(col,data)
    #     # filter_data = xw.apps.keys()
    #     # print(filter_data)
    #     # return filter_data
    #     pass
    #
    # # 删除过滤条件
    # def remove_filter(self):
    #     pass
    #
    # # 对多列进行筛选
    # def multi_filter(self):
    #     pass
    #
    # # 宏
    # def run_macro(self, name):
    #     # self.workbook.sheets[0].range('A1').value = 'Hello World!'
    #     self.workbook.macro(name=name)
    #     return
    #
    # # 合并单元格
    # def merge_cell(self, range_num):
    #     self.original_sheet = self.original_sheet.range(range_num).api.merge()
    #     return self.original_sheet
    #
    # # 插入行
    # def insert_rows(self, range_num):
    #     self.original_sheet = self.original_sheet.api.Rows(range_num).Insert()
    #     return self.original_sheet
    #
    # # 插入列
    # def insert_columns(self, range_num):
    #     self.original_sheet = self.original_sheet.api.Columns(range_num).Insert()
    #     return self.original_sheet
    #
    # # 删除
    # def delete(self, range_cell):
    #     self.original_sheet = self.original_sheet.range(range_cell).delete()
    #     return self.original_sheet
    #
    # # 删除重复
    # def remove_duplicate(self, rows, columns):
    #     self.original_sheet = self.original_sheet.range(rows, columns).api.RemoveDuplicates()
    #     return self.original_sheet
    #
    # # 添加图片
    # def add_picture(self, file):
    #     self.original_sheet.pictures.add(os.path.join(os.getcwd(), file))
    #     return
    #
    # # 获取行高
    # def get_row_height(self, rows):
    #     row_height = self.original_sheet.range(rows).row_height
    #     return row_height
    #
    # # 设置行高
    # def set_row_height(self, colnum, rownum, height):
    #     self.original_sheet.range(colnum, rownum).row_height = height
    #     return
    #
    # # 获取宽度
    # def get_col_width(self, colnum):
    #     col_width = self.original_sheet.range(colnum).column_width
    #     return col_width
    #
    # # 设置宽度
    # def set_col_width(self, rownum, colnum, width):
    #     self.original_sheet.range(rownum, colnum).column_width = width
    #     return
    #
    # # 获取指定范围的公式
    # def get_formula(self, range_col_row):
    #     formula = self.original_sheet.range(range_col_row).formula
    #     return formula
    #
    # # 设置指定范围的公式
    # def set_formula(self, range_col_row, formula):
    #     self.original_sheet.range(range_col_row).formula = formula
    #     return
    #
    # # 获取指定范围的样式
    # def get_style(self, range_cell):
    #     self.style.append(self.original_sheet.range(range_cell).api.Font.Size)
    #     self.style.append(self.original_sheet.range(range_cell).api.Font.ColorIndex)
    #     self.style.append(self.original_sheet.range(range_cell).api.Font.Name)
    #     self.style.append(self.original_sheet.range(range_cell).color)
    #     return self.style
    #
    # # 设置指定范围的样式
    # def set_style(self, range_cell, fontsize, fontcolor, fontname, bgcolor):
    #     self.original_sheet.range(range_cell).api.Font.Size = fontsize
    #     self.original_sheet.range(range_cell).api.Font.ColorIndex = fontcolor
    #     self.original_sheet.range(range_cell).api.Font.Name = fontname
    #     self.original_sheet.range(range_cell).color = bgcolor
    #     return
    #
    # # 获取指定范围的注释
    # def get_comment(self, text, author):
    #     # data = self.sheet.range(cell)
    #     # data = self.sheet.range(cell).comment()
    #     data = Comment(text=text, author=author)
    #     return data
    #
    # # 往指定范围插入注释
    # def set_comment(self, cell, text, author):
    #     self.original_sheet[cell].comment = Comment(text=text, author=author)
    #     return
    #
    # # 替换指定内容
    # def replace_data(self, text, replacement, match_case=False):
    #     data = self.original_sheet.range('A1').expand().value
    #     for i in range(len(data)):
    #         for j in range(len(data[i])):
    #             # print(data[i][j)
    #             if text == data[i][j]:
    #                 self.original_sheet.range(i, j).value = replacement
    #                 break
    #             else:
    #                 pass
    #
    #     return
    #
    # # 转化成pdf
    # def to_pdf(self, file):
    #     self.workbook.save(file)
    #     return
    #
    # # 激活当前sheet
    # def activate(self):
    #     self.original_sheet.activate()
    #     return self.original_sheet
    #
    # # 设置指定范围的数值格式
    # def set_number_format(self, range_num):
    #     self.original_sheet.range(range_num).api.NumberFormat = self.style
    #     return
