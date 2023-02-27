from PySide6 import QtWidgets

from qtefun.组件.组件公共类 import 组件公共类


# https://doc.qt.io/qt-6/qfontcombobox.html
# 事件
# void	currentFontChanged(const QFont &font)

class 字体选择框(组件公共类):
    对象 = None  # type: QtWidgets.QFontComboBox

    def 取字体(self):
        return self.对象.currentFont()

    def 取字体名称(self):
        return self.对象.currentFont().family()

    def 置字体(self, 字体):
        self.对象.setCurrentFont(字体)

    def 绑定事件字体被改变(self, 回调函数):
        self.对象.currentFontChanged.connect(回调函数)
