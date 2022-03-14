# 说明

1. 本模块两个类型：
   1. HilandExcel 是在 excel 文件这个层面上进行的逻辑包装
   2. HilandSheet 是在 sheet 表格这个层面上进行的逻辑包装

2. 因为涉及到资源释放，因此在使用HilandExcel的时候，建议使用 with 的方式，如下：
   ```
   with HilandExcel(file_full_name) as excel:
        actual = excel.get_sheets_count()
        expected = 3
        assert actual == expected
   ```
3. 使用时不要直接创建 HilandSheet，请通过 `HilandExcel.get_sheet(s)` 方法获取


