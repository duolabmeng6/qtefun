from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QTime, QDate

from qtefun.组件.组件公共类 import 组件公共类

# https://doc.qt.io/qt-6/qdateedit.html
# void	dateChanged(QDate date) 日期被改变
# void	dateTimeChanged(const QDateTime &datetime) 日期时间被改变
# void	timeChanged(QTime time) 时间被改变


class 日期编辑框(组件公共类):
    对象 = None  # type: QtWidgets.QDateEdit

    def 取日期(self):
        return self.对象.date()

    def 置日期(self, 年, 月, 日):
        return self.对象.setDate(QDate(年, 月, 日))

    def 绑定事件日期被改变(self, 回调函数):
        self.对象.dateChanged.connect(回调函数)


