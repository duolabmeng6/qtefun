from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QTime, QDate, QDateTime
from PySide6.QtGui import QImage, QColor

from qtefun.组件.组件公共类 import 组件公共类

# https://doc.qt.io/qt-6/qdatetimeedit.html
# void	dateChanged(QDate date) 日期被改变
# void	dateTimeChanged(const QDateTime &datetime) 日期时间被改变
# void	timeChanged(QTime time) 时间被改变


class 日期时间编辑框(组件公共类):
    对象 = None  # type: QtWidgets.QDateTimeEdit

    def 取日期(self):
        return self.对象.date()

    def 置日期(self, 年, 月, 日):
        return self.对象.setDate(QDate(年, 月, 日))

    def 取时间(self):
        return self.对象.time()

    def 置时间(self, 时, 分, 秒):
        return self.对象.setTime(QTime(时, 分, 秒))

    def 取日期时间(self):
        return self.对象.dateTime()

    def 置日期时间(self, 年, 月, 日, 时, 分, 秒):
        return self.对象.setDateTime(QDateTime(年, 月, 日, 时, 分, 秒))

    def 绑定事件时间被改变(self, 回调函数):
        self.对象.timeChanged.connect(回调函数)

    def 绑定事件日期被改变(self, 回调函数):
        self.对象.dateChanged.connect(回调函数)

    def 绑定事件日期时间被改变(self, 回调函数):
        self.对象.dateTimeChanged.connect(回调函数)


