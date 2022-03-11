"""
 * @file   : hilandSheet.py
 * @time   : 20:45
 * @date   : 2021/11/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os

from openpyxl.comments import Comment


class HilandSheet:
    def __init__(self, sheet=None, file_with_path=None, sheet_marker=0):
        if sheet:
            self.original_sheet = sheet
        else:
            self.workbook = open(file_with_path)
            self.original_sheet = self.workbook.sheets[sheet_marker]

        # print(self.sheet)
        self.cell = None
        self.my_range = None
        self.style = []

    # 读取数据
    def read(self, range_num):
        # 获取单元格值到列表
        value = self.original_sheet.range(range_num).value
        return value

    # 写入数据
    def write(self, range_num, write_range):
        self.original_sheet.range(range_num).value = write_range
        return

    # 复制
    def copy(self, sheet_name, range_col_row):
        self.my_range = self.original_sheet.Range(sheet_name, range_col_row).value
        return self.my_range

    # 粘贴
    def paste(self, sheet_name, range_col_row):
        self.original_sheet.Range(sheet_name, range_col_row).value = self.my_range
        return

    # 粘贴数据
    def paste_range(self, sheet_name, range_col_row):
        self.original_sheet.Range(sheet_name, range_col_row).value = self.my_range
        return

    def get_column_count(self):
        """
        获取行数
        :return:
        """
        col_value = self.original_sheet.used_range.last_cell.column
        return col_value

    # 获取列数
    def get_row_count(self):
        row_value = self.original_sheet.used_range.last_cell.row
        return row_value

    # 排序
    def sort(self, cell_pos):
        self.original_sheet.range(cell_pos).api.Sort(Key1=self.original_sheet.range(cell_pos).api, Order1=1)
        # print(self.sheet.name)
        # data = self.sheet.range(cell_pos).value
        # print(data)
        # key = data.sort()
        # print(key)
        # for i in key:
        #     self.sheet.range(cell_pos).value = i
        # self.sheet.range(cell_pos).api.Sort(key=key,Order=2)
        # data = self.sheet.range(cell_pos).value
        # print(data)
        # print(data)
        return

    # 过滤条件
    def filter(self, col, data):
        # filter_data = self.sheet.range.filter(col,data)
        # filter_data = xw.apps.keys()
        # print(filter_data)
        # return filter_data
        pass

    # 删除过滤条件
    def remove_filter(self):
        pass

    # 对多列进行筛选
    def multi_filter(self):
        pass

    # 宏
    def run_macro(self, name):
        # self.workbook.sheets[0].range('A1').value = 'Hello World!'
        self.workbook.macro(name=name)
        return

    # 合并单元格
    def merge_cell(self, range_num):
        self.original_sheet = self.original_sheet.range(range_num).api.merge()
        return self.original_sheet

    # 插入行
    def insert_rows(self, range_num):
        self.original_sheet = self.original_sheet.api.Rows(range_num).Insert()
        return self.original_sheet

    # 插入列
    def insert_columns(self, range_num):
        self.original_sheet = self.original_sheet.api.Columns(range_num).Insert()
        return self.original_sheet

    # 删除
    def delete(self, range_cell, insertDirection=None):
        self.original_sheet = self.original_sheet.range(range_cell).delete()
        return self.original_sheet

    # 删除重复
    def remove_duplicate(self, rows, columns):
        self.original_sheet = self.original_sheet.range(rows, columns).api.RemoveDuplicates()
        return self.original_sheet

    # 添加图片
    def add_picture(self, file):
        # self.sheet.Range(col, row).append(file)
        self.original_sheet.pictures.add(os.path.join(os.getcwd(), file))
        return

    # 获取行高
    def get_row_height(self, rows):
        row_height = self.original_sheet.range(rows).row_height
        return row_height

    # 设置行高
    def set_row_height(self, colnum, rownum, height):
        self.original_sheet.range(colnum, rownum).row_height = height
        return

    # 获取宽度
    def get_col_width(self, colnum):
        col_width = self.original_sheet.range(colnum).column_width
        return col_width

    # 设置宽度
    def set_col_width(self, rownum, colnum, width):
        self.original_sheet.range(rownum, colnum).column_width = width
        return

    # 获取指定范围的公式
    def get_formula(self, range_col_row):
        formula = self.original_sheet.range(range_col_row).formula
        return formula

    # 设置指定范围的公式
    def set_formula(self, range_col_row, formula):
        self.original_sheet.range(range_col_row).formula = formula
        return

    # 获取指定范围的样式
    def get_style(self, range_cell):
        self.style.append(self.original_sheet.range(range_cell).api.Font.Size)
        self.style.append(self.original_sheet.range(range_cell).api.Font.ColorIndex)
        self.style.append(self.original_sheet.range(range_cell).api.Font.Name)
        self.style.append(self.original_sheet.range(range_cell).color)
        return self.style

    # 设置指定范围的样式
    def set_style(self, range_cell, fontsize, fontcolor, fontname, bgcolor):
        # fontsize, fontcolor, fontname, bgcolor
        self.original_sheet.range(range_cell).api.Font.Size = fontsize
        self.original_sheet.range(range_cell).api.Font.ColorIndex = fontcolor
        self.original_sheet.range(range_cell).api.Font.Name = fontname
        self.original_sheet.range(range_cell).color = bgcolor
        return

    # 获取指定范围的注释
    def get_comment(self, text, author):
        # data = self.sheet.range(cell)
        # data = self.sheet.range(cell).comment()
        data = Comment(text=text, author=author)
        return data

    # 往指定范围插入注释
    def set_comment(self, cell, text, author):
        self.original_sheet[cell].comment = Comment(text=text, author=author)
        return

    # 替换指定内容
    def replace_data(self, text, replacement, match_case=False):
        data = self.original_sheet.range('A1').expand().value
        # print(data)
        for i in range(len(data)):
            for j in range(len(data[i])):
                # print(data[i][j)
                if text == data[i][j]:
                    self.original_sheet.range(i, j).value = replacement
                    break
                    # data[i][j]=repalcement
                else:
                    pass

        return

    # 转化成pdf
    def to_pdf(self, file):
        self.workbook.save(file)
        return

    # 激活当前sheet
    def activate(self):
        self.original_sheet.activate()
        return self.original_sheet

    # 设置指定范围的数值格式
    def set_number_format(self, range_num):
        self.original_sheet.range(range_num).api.NumberFormat = self.style
        return
