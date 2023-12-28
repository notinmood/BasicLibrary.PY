# 说明

## 开发说明

1. 各功能按照相近程度进行划分子包：不同的功能划入不同的子包。
2. 常用的功能可以通过别名的方式放入 `BasicLibrary` 根目录下的 `__init__.py` 文件内

## 部署说明

1. 以下两个文件复制到项目根目录下
    1. `__projectConfig.ini` 改名为 `_projectConfig.ini`
    2. `__projectHelper.py`  改名为 `_projectHelper.py`

2. 如果有敏感信息(比如账号口令等)不适合写在ini文件内的，可以将.env.default文件拷贝到文件 _projectConfig.ini所在的项目根目录,然后改名为 .env,然后再.env内配置这些信息.
   (ini文件是嵌入到vcs系统的，但.env是不嵌入vcs系统的)
