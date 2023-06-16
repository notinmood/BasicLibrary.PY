# 企业级的Python类库

```
@emailto: 9727005@qq.com
@creator: ShanDong Xiedali
@company: HiLand & RainyTop
```

整理常用的代码块，形成企业级的类库工具，供更多项目使用。

## 【零】目录格式

1. 最外层是整个项目的根目录(本项目中为 BasicLibrary.PY)，这个目录作为 git 的根目录。
2. 根目录下分布"部署文件""说明文件"等周边辅助文件(比如 setup.py、README.md等)
3. 根目录下用 Python 包的形式架构项目的业务逻辑代码(本项目下为 BasicLibrary)
   (一般每个项目只架构一个根 Python 包,然后再决定是在根包下再架构子包，还是在根包下直接写 ***.py 代码)

## 【一】发布步骤：

1. 打开本项目的"终端"窗口(或者通过 windows 的资源管理器定位到本项目 setup.py 所在的目录)
2. 打开修改 setup.py 文件 `VERSION = '0.4.3'`为新的值
3. 运行命令 `python setup.py sdist`
4. 运行命令 `twine upload dist/*`

## 【二】其他

将本项目需求的第三方软件包统一组织在 requirements.txt 文件内。

1. 组织第三方软件包进入文件的命令是：`pip freeze > requirements.txt`
2. 重新安装所需的各第三方包的命令为：`pip install -r requirements.txt`

## 【三】部署


### 1. 库安装（更新）说明
更新公司类库 BasicLibrary.PY 的命令：

```
pip install BasicLibrary.PY -U
# (因为本地的pip通常都为了加速，进行过换源处理了，换源之后缓存更新会比较慢。
# 所以为了使用最新的库功能，可以使用原始的PIPY源，代码如下：)
pip install BasicLibrary.PY -U -i https://pypi.org/simple
```
### 2. 库使用说明

   1. 以下两个文件复制到项目根目录下
       1. `__projectConfig.ini` 改名为 `_projectConfig.ini`
       2. `__projectHelper.py` 改名为 `_projectHelper.py`

   2. 如果有敏感信息(比如账号口令等)不适合写在 ini 文件内的，可以将 `.env.default` 文件拷贝到文件 `_projectConfig.ini` 所在的项目根目录,然后改名为 `.env`,然后在 .env 文件内配置这些信息. (
      ini 文件是嵌入到 vcs 系统的，但 .env 是不嵌入 vcs 系统的)
