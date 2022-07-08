from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QColor

from qtefun.组件.组件公共类 import 组件公共类


class 纯文本编辑框(组件公共类):
    """
    事件

    def blockCountChanged (newBlockCount)   - 当文本块数发生变化时触发

    def copyAvailable (b) - 当前文本被拷贝到剪贴板时触发

    def cursorPositionChanged () - 光标位置已更改

    def modificationChanged (arg__1) - 修改已更改

    def redoAvailable (b) - 当前文本可以重做时触发

    def selectionChanged () - 选择已更改

    def textChanged () - 文本已更改

    def undoAvailable (b) - 当前文本可以撤销时触发

    def updateRequest (rect, dy) - 更新请求

    """
    对象 = None  # type: QtWidgets.QPlainTextEdit

    # 获取标题
    @property
    def 内容(self):
        return self.对象.toPlainText()

    # 设置内容
    @内容.setter
    def 内容(self, value: str):
        print("设置标题", value)
        return self.对象.setPlainText(value)

    def 绑定事件内容被改变(self, 回调函数):
        return self.对象.textChanged.connect(回调函数)

