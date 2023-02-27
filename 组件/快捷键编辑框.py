from PySide6 import QtWidgets

from qtefun.组件.组件公共类 import 组件公共类

# https://doc.qt.io/qt-6/qkeysequenceedit.html
# 事件
# void	editingFinished() # 编辑完成
# void	keySequenceChanged(const QKeySequence &keySequence) # 快捷键被改变

class 快捷键编辑框(组件公共类):

    对象 = None  # type: QtWidgets.QKeySequenceEdit

    # 获取标题
    @property
    def 内容(self):
        return self.ui.keySequenceEdit.keySequence().toString()

    # 设置内容
    @内容.setter
    def 内容(self, value: str):
        print("设置标题", value)
        return self.对象.setKeySequence(value)

    def 取快捷键(self):
        return self.对象.keySequence()

    def 置快捷键(self, 快捷键):
        self.对象.setKeySequence(快捷键)

    def 取快捷键文本(self):
        return self.对象.keySequence().toString()

    def 置快捷键文本(self, 快捷键文本):
        self.对象.setKeySequence(快捷键文本)

    def 取快捷键文本列表(self):
        return self.对象.keySequence().toString().split(", ")

    def 置快捷键文本列表(self, 快捷键文本列表):
        self.对象.setKeySequence(快捷键文本列表)


    def 绑定事件按键被改变(self, 回调函数):
        """
        快捷键被改变
        :param 回调函数: 回调函数(const QKeySequence &keySequence)
        """
        return self.对象.keySequenceChanged.connect(回调函数)

    def 绑定事件编辑完成(self, 回调函数):
        return self.对象.editingFinished.connect(回调函数)
