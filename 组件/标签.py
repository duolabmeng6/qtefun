from PySide6 import QtWidgets

from qtefun.组件.组件公共类 import 组件公共类


class 标签(组件公共类):
    对象 = None # type: QtWidgets.QLabel

    # 获取标题
    @property
    def 标题(self):
        return self.对象.text()

    # 设置标题
    @标题.setter
    def 标题(self, value: str):
        return self.对象.setText(value)
