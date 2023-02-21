from PySide6 import QtWidgets

from qtefun.组件.组件公共类 import 组件公共类


# https://doc.qt.io/qt-6/qtabwidget.html
# 选择夹
# 事件
# void	currentChanged(int index) 现行子夹被改变
# void	tabBarClicked(int index) 子夹被点击
# void	tabBarDoubleClicked(int index) 子夹被双击
# void	tabCloseRequested(int index) 子夹关闭


class 选择夹(组件公共类):
    对象 = None  # type: QtWidgets.QTabWidget

    @property
    def 现行子夹(self):
        return self.currentIndex()

    @现行子夹.setter
    def 现行子夹(self, 索引: int):
        return self.setCurrentIndex(索引)

    def 取子夹数目(self):
        return self.count()

    def 取子夹名称(self, 索引: int):
        return self.tabText(索引)

    def 置子夹名称(self, 索引: int, 名称: str):
        return self.setTabText(索引, 名称)

    def 置子夹可用(self, 索引: int, 是否可用: bool):
        return self.setTabEnabled(索引, 是否可用)
    def 置子夹可见(self, 索引: int, 是否可见: bool):
        return self.setTabVisible(索引, 是否可见)

    # void	currentChanged(int index) 现行子夹被改变
    def 绑定事件当前子夹改变(self, 函数):
        self.对象.currentChanged.connect(函数)
    # void	tabBarClicked(int index) 被点击
    def 绑定事件子夹被点击(self, 函数):
        self.对象.tabBarClicked.connect(函数)
    # void	tabBarDoubleClicked(int index) 被双击
    def 绑定事件子夹被双击(self, 函数):
        self.对象.tabBarDoubleClicked.connect(函数)
    # void	tabCloseRequested(int index) 选项卡关闭
    def 绑定事件子夹被关闭(self, 函数):
        self.对象.tabCloseRequested.connect(函数)
