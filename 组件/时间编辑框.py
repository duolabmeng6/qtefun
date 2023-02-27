from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QTime
from PySide6.QtGui import QImage, QColor

from qtefun.组件.组件公共类 import 组件公共类

# https://doc.qt.io/qt-6/qdatetimeedit.html
# void	dateChanged(QDate date) 日期被改变
# void	dateTimeChanged(const QDateTime &datetime) 日期时间被改变
# void	timeChanged(QTime time) 时间被改变


class 时间编辑框(组件公共类):
    对象 = None  # type: QtWidgets.QTimeEdit

    def 取时间(self):
        return self.对象.time()

    def 置时间(self, 时, 分, 秒):
        return self.对象.setTime(QTime(时, 分, 秒))

    def 绑定事件时间被改变(self, 回调函数):
        self.对象.timeChanged.connect(回调函数)
