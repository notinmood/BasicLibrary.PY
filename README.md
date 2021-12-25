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
1. 运行命令 "python setup.py sdist"
2. 运行命令 "twine upload dist/*"

## 【二】其他

将本项目需求的第三方软件包统一成requirements.txt文件的命令是：pip freeze > requirements.txt

## 【三】部署

以下两个文件复制到项目根目录下

1. __ProjectConfig.ini 改名为 _ProjectConfig.ini
2. __ProjectHelper.py 改名为 _ProjectHelper.py