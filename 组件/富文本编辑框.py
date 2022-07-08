from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QColor

from qtefun.组件.组件公共类 import 组件公共类


class 富文本编辑框(组件公共类):
    """
    事件

    copyAvailable(bool) - 当前文本被拷贝到剪贴板时触发
    currentCharFormatChanged(QTextCharFormat) - 当前文本格式发生变化时触发 内容被改变
    cursorPositionChanged () - 当前光标位置发生变化时触发
    redoAvailable(bool) - 当前文本可以重做时触发
    selectionChanged() - 当前文本选择发生变化时触发
    textChanged () - 当前文本发生变化时触发
    undoAvailable(bool) - 当前文本可以撤销时触发

    """
    对象 = None  # type: QtWidgets.QTextEdit

    # 获取标题
    @property
    def 内容(self):
        return self.对象.toPlainText()

    # 设置内容
    @内容.setter
    def 内容(self, value: str):
        print("设置标题", value)
        return self.对象.setText(value)

    def 绑定事件内容被改变(self, 回调函数):
        return self.对象.textChanged.connect(回调函数)

