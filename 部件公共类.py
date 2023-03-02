from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QColor


class 部件公共类(QtWidgets.QWidget):


    # 获取窗口标题
    @property
    def 标题(self):
        return self.windowTitle()

    # 设置窗口标题
    @标题.setter
    def 标题(self, value: str):
        return self.setWindowTitle(value)

    # 获取窗口宽度
    @property
    def 宽度(self):
        return self.width()

    # 设置窗口宽度
    @宽度.setter
    def 宽度(self, value: int):
        return self.setFixedWidth(value)

    # 获取窗口高度
    @property
    def 高度(self):
        return self.height()

    # 设置窗口高度
    @高度.setter
    def 高度(self, value: int):
        return self.setFixedHeight(value)

    # 获取窗口左边
    @property
    def 左边(self):
        return self.x()

    # 设置窗口左边
    @左边.setter
    def 左边(self, value: int):
        return self.move(value, self.y())

    # 获取窗口上边
    @property
    def 顶边(self):
        return self.y()

    # 设置窗口顶边
    @顶边.setter
    def 顶边(self, value: int):
        return self.move(self.x(), value)

    # 获取窗口右边
    @property
    def 右边(self):
        return self.x() + self.width()

    # 设置窗口右边
    @右边.setter
    def 右边(self, value: int):
        return self.move(value - self.width(), self.y())

    # 获取窗口下边
    @property
    def 下边(self):
        return self.y() + self.height()

    # 设置窗口下边
    @下边.setter
    def 下边(self, value: int):
        return self.move(self.x(), value - self.height())

    # 获取窗口大小
    @property
    def 大小(self):
        return self.size()

    # 设置窗口大小
    @大小.setter
    def 大小(self, value: tuple):
        return self.setFixedSize(value)

    # 获取窗口位置
    @property
    def 位置(self):
        return self.pos()

    # 设置窗口位置
    @位置.setter
    def 位置(self, value: tuple):
        return self.move(value)

    # 获取窗口是否可见
    @property
    def 可视(self):
        return self.isVisible()

    # 设置窗口是否可见
    @可视.setter
    def 可视(self, value: bool):
        return self.setVisible(value)

    # 获取屏幕宽度
    def 取屏幕宽度(self):
        return self.screen().physicalSize().width()

    # 获取屏幕高度
    def 取屏幕高度(self):
        return self.screen().physicalSize().height()

    # 获取屏幕分辨率
    def 取屏幕分辨率(self):
        return self.screen().physicalSize()

    # 移动
    def 移动(self, x: int, y: int):
        return self.move(x, y)

    # 移动到屏幕中间
    def 移动到屏幕中间(self):
        return self.move(self.取屏幕宽度() / 2 - self.width() / 2, self.取屏幕高度() / 2 - self.height() / 2)

    # 移动到屏幕右下角
    def 移动到屏幕右下角(self):
        return self.move(self.取屏幕宽度() - self.width(), self.取屏幕高度() - self.height())

    # 移动到屏幕左上角
    def 移动到屏幕左上角(self):
        return self.move(0, 0)

    # 移动到屏幕左下角
    def 移动到屏幕左下角(self):
        return self.move(0, self.取屏幕高度() - self.height())

    # 移动到屏幕右上角
    def 移动到屏幕右上角(self):
        return self.move(self.取屏幕宽度() - self.width(), 0)

    # 移动到屏幕中间
    def 移动到屏幕中间(self):
        return self.move(self.取屏幕宽度() / 2 - self.width() / 2, self.取屏幕高度() / 2 - self.height() / 2)

    # 设置背景颜色
    def 设置背景颜色(self, color: QColor):
        return self.setStyleSheet("background-color: %s;" % color.name())

    # 设置背景图片
    def 设置背景图片(self, image: QImage):
        return self.setStyleSheet("background-image: url(%s);" % image.toImage().toBase64().decode())

    def 置鼠标样式(self, 样式: Qt.CursorShape):
        '''
        https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html?highlight=cursorshape#PySide6.QtCore.PySide6.QtCore.Qt.CursorShape
        '''
        return self.setCursor(样式)

    # 设置提示文本
    def 设置提示文本(self, text: str):
        return self.setToolTip(text)
