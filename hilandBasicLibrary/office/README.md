# 说明

本模块两个类型：
HilandExcel 是在 excel 文件这个层面上进行的逻辑包装
HilandSheet 是在 sheet 表格这个层面上进行的逻辑包装

使用时最好不要直接创建 HilandSheet，请通过 HilandExcel.get_sheet(s) 方法获取
TODO:本模块的部分方法没有验证，使用的时候请二次验证和修改