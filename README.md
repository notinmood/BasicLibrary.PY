# 企业级的Python类库

```
@emailto: 9727005@qq.com
@creator: ShanDong Xiedali
@company: HiLand & RainyTop
```

整理常用的代码块，形成企业级的类库工具，供更多项目使用。

## 【零.1】目录格式

1. 最外层是整个项目的根目录(本项目中为 BasicLibrary.PY)，这个目录作为 git 的根目录。
2. 根目录下分布"部署文件""说明文件"等周边辅助文件(比如 setup.py、README.md等)
3. 根目录下用 Python 包的形式架构项目的业务逻辑代码(本项目下为 BasicLibrary)
   (一般每个项目只架构一个根 Python 包,然后再决定是在根包下再架构子包，还是在根包下直接写 ***.py 代码)

## 【零.2】命名规则

1. 文件名、文件夹名: 全部小写开头；如果多个单词第一单词全部小写，第二、三个单词首字母大写，单词之间不用下划线连接，不使用空格。
2. 文件内的类型名称: 每个单词的首字母都大写，单词之间不用下划线连接，不使用空格。
3. 函数名、变量名: 每个单词的首字母都小写，单词之间用下划线连接，不使用空格。
4. 常量名: 全部大写开头，单词之间不用下划线连接，不使用空格。
5. 不供外部调用的模块或者文件名称，统一使用“_”(单下划线)或“__”(双下划线)开头。其余同第2条。
6. 以`“_”“__”`开头命名的模块或者文件，内部的类型名称，正常命名（即不使用“_”和“__”开头）。
7. 不供外部调用的函数、变量、常量: 统一使用“_”(单下划线)或“__”(双下划线)开头。其余同第3条。

## 【一】发布步骤：

1. 打开文件`pyproject.toml`,修改`version = '0.4.3'`为新的值
2. 打开本项目的"终端"窗口(或者通过 windows 的资源管理器定位到本项目根目录所在的位置)
3. 打包项目。运行命令：`poetry build`
4. 发布项目。运行命令：`poetry publish`

## 【二】其他

将本项目需求的第三方软件包统一组织在 `pyproject.toml` 文件内。

1. 安装第三方软件包。运行命令：`poetry add 包名`
2. 更新第三方软件包。运行命令：`poetry update 包名`
3. 删除第三方软件包。运行命令：`poetry remove 包名`
4. 查看已安装的第三方软件包。运行命令：`poetry show`

## 【三】本库的使用说明

### 1. 库安装（更新）说明

更新公司类库 BasicLibrary.PY 的命令：

1. 传统pip方式
    ```shell
    pip install BasicLibrary.PY -U
    # (因为本地的pip通常都为了加速，进行过换源处理了，换源之后缓存更新会比较慢。
    # 所以为了使用最新的库功能，可以使用原始的PIPY源，代码如下：)
    pip install BasicLibrary.PY -U -i https://pypi.org/simple
    ```
2. poetry方式
    ```shell
    poetry add BasicLibrary.PY
    poetry update BasicLibrary.PY
    poetry remove BasicLibrary.PY
    ```

### 2. 库使用说明

1. 以下两个文件复制到项目根目录下
    1. `__projectConfig.ini` 改名为 `_projectConfig.ini`
    2. `__projectHelper.py` 改名为 `_projectHelper.py`

2. 如果有敏感信息(比如账号口令等)不适合写在 ini 文件内的，可以将 `.env.default` 文件拷贝到文件 `_projectConfig.ini`
   所在的项目根目录,然后改名为 `.env`,然后在 .env 文件内配置这些信息. (
   ini 文件是嵌入到 vcs 系统的，但 .env 是不嵌入 vcs 系统的)
