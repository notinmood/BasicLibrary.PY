"""
 * @file   : PhotoShopHelper.py
 * @time   : 9:56
 * @date   : 2023/12/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from os import PathLike

from photoshop import Session
from photoshop.api import ActionDescriptor

from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.io.fileHelper import FileHelper


class PhotoShopHelper(object):
    """
    Photoshop辅助类
    本类方法适用于Photoshop软件的第三方类库`photoshop_python_api`，使用前请先安装本类库（`pip install photoshop_python_api`）；
    如果需要适配其他第三方类库的辅助功能，请重新实现。
    """

    @classmethod
    def find_layer(cls, layers, layer_code, layer_path_seperator="//"):
        """
        根据图层名称遍历（包括嵌套图层）各图层查找目标图层
        :param layer_path_seperator:如果layer_code是图层的路径，则需要本参数指定路径的分隔符，默认为"//"
        :param layers:待查找的图层列表（即到此集合中查找目标图层）
        :param layer_code:图层的名字name（字符串）或者图层的索引号index（数字），
                           1. 如果为字符串，可以包含用双斜线分割的图层路径，如：layer1//layer2//layer3；也可以是仅仅图层的名字（系统会自动迭代查找）。
                           2. 如果为数字，则表示图层的索引号，从0开始。
        :return:
        """
        # 判定layer_name的数据类型是否为数字
        if isinstance(layer_code, int) and layers[layer_code]:
            return layers[layer_code]
        pass

        # 判定layer_name的数据类型是否为字符串
        if isinstance(layer_code, str):
            if StringHelper.is_contains(layer_code, layer_path_seperator):
                return cls.__find_layer_by_path(layers, layer_code, layer_path_seperator)
            pass

            # 遍历图层列表
            for layer in layers:
                if layer.name == layer_code:
                    return layer
                pass

                # 如果当前图层是一个图层组，递归查找子图层
                if layer.blendMode == 1:  # blendMode为1表示图层组；blendMode为2表示一个普通图层
                    found_layer = cls.find_layer(layer.layers, layer_code)
                    if found_layer:
                        return found_layer
                    pass
                pass
            pass
        pass

        return None

    @classmethod
    def __find_layer_by_path(cls, layers, layer_path, layer_path_seperator="//"):
        def find_layer_recursive(_layers, path):
            for layer in _layers:
                if layer.name == path[0]:
                    if len(path) == 1:
                        return layer
                    else:
                        return find_layer_recursive(layer.layers, path[1:])
                    pass
                pass
            pass

            return None

        return find_layer_recursive(layers, layer_path.split(layer_path_seperator))

    pass

    @classmethod
    def replace_image(cls, psd_full_name: PathLike, layer_code: str, new_image_full_name: PathLike,
                      is_auto_close: bool = True):
        """
        替换psd文件中的图层图片
        :param psd_full_name: psd文件的全路径
        :param layer_code: 图层的代码：图层的名称、索引号或者图层的路径
        :param new_image_full_name: 新的图片文件的全路径
        :param is_auto_close: 是否自动关闭psd文件
        :return:
        """
        if not FileHelper.is_file(new_image_full_name):
            return
        pass

        if not FileHelper.is_file(psd_full_name):
            return
        pass

        with Session(psd_full_name, action="open") as ps:
            app = ps.app
            document = ps.active_document

            # 查找并设置活动图层
            layer_matched = cls.find_layer(document.layers, layer_code)
            if not layer_matched:
                return
            pass

            document.activeLayer = layer_matched
            replace_contents = app.stringIDToTypeID("placedLayerReplaceContents")
            id_null = app.charIDToTypeID("null")
            action_descriptor = ActionDescriptor()
            action_descriptor.putPath(id_null, new_image_full_name)
            app.executeAction(replace_contents, action_descriptor)

            document.save()

            if is_auto_close:
                document.close()
                ps.close()
            pass
        pass

    pass


pass