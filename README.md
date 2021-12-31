企业级的Python类库
--

```
@emailto: 9727005@qq.com
@creator: ShanDong Xiedali
@company: HiLand & RainyTop
```

收集常用的代码块，形成类库工具，在多项目中共同使用。

## 【零】目录格式

1. 最外层是整个项目的根目录(本项目中为BasicLibrary.PY)，这个目录作为git的根目录。
2. 根目录下分布"部署文件""说明文件"等周边辅助文件(比如setup.py、README.md等)
3. 根目录下用Python包的形式架构项目的业务逻辑代码(本项目下为hilandBasicLibrary)
   (一般每个项目只架构一个根Python包,然后再根包下决定是否再架构子包，还是在根包下直接写***.py代码)

## 【一】发布步骤：

0. 打开本项目的"终端"窗口(或者通过windows的资源管理器定位到本项目setup.py所在的目录)
1. 打开修改setup.py文件 VERSION = '0.4.3'为新的值
2. 运行命令 "python setup.py sdist"
3. 运行命令 "twine upload dist/*"

## 【二】其他

将本项目需求的第三方软件包统一组织在requirements.txt文件内。

1. 组织第三方软件包进入文件的命令是：pip freeze > requirements.txt
2. 重新安装所需的各第三方包的命令为: pip install -r requirements.txt

## 【三】部署

1. 以下两个文件复制到项目根目录下
   1. __projectConfig.ini 改名为 _projectConfig.ini
   2. __projectHelper.py 改名为 _projectHelper.py

2. 如果有敏感信息(比如账号口令等)不适合写在ini文件内的，可以将.env.default文件拷贝到文件 _projectConfig.ini所在的项目根目录,然后改名为 .env,然后再.env内配置这些信息. (ini文件是嵌入到vcs系统的，但.env是不嵌入vcs系统的)