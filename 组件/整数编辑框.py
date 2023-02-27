from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QTime
from PySide6.QtGui import QImage, QColor

from qtefun.组件.组件公共类 import 组件公共类

# https://doc.qt.io/qt-6/qspinbox.html
# void	textChanged(const QString &text) 文本被改变
# void	valueChanged(int i)   值被改变


class 整数编辑框(组件公共类):
    对象 = None  # type: QtWidgets.QSpinBox

    def 取值(self):
        return self.对象.value()

    def 取最小值(self):
        return self.对象.minimum()

    def 取最大值(self):
        return self.对象.maximum()

    def 置值(self, 值):
        self.对象.setValue(值)

    def 置最小值(self, 值):
        self.对象.setMinimum(值)

    def 置最大值(self, 值):
        self.对象.setMaximum(值)

    def 置步长(self, 值):
        self.对象.setSingleStep(值)

    def 取步长(self):
        return self.对象.singleStep()

    def 置前缀(self, 值):
        self.对象.setPrefix(值)

    def 取前缀(self):
        return self.对象.prefix()

    def 置后缀(self, 值):
        self.对象.setSuffix(值)

    def 取后缀(self):
        return self.对象.suffix()

    def 绑定事件文本被改变(self, 回调函数):
        self.对象.textChanged.connect(回调函数)

    def 绑定事件值被改变(self, 回调函数):
        self.对象.valueChanged.connect(回调函数)

