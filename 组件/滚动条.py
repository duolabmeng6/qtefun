from PySide6 import QtWidgets

from qtefun.组件.组件公共类 import 组件公共类


# https://doc.qt.io/qt-6/qscrollbar.html
# 事件
# void	actionTriggered(int action)
# void	rangeChanged(int min, int max)
# void	sliderMoved(int value)
# void	sliderPressed()
# void	sliderReleased()
# void	valueChanged(int value)

class 滚动条(组件公共类):
    对象 = None  # type: QtWidgets.QScrollBar

    def 取最小值(self):
        return self.对象.minimum()

    def 取最大值(self):
        return self.对象.maximum()

    def 取当前值(self):
        return self.对象.value()

    def 置最小值(self, 最小值):
        self.对象.setMinimum(最小值)

    def 置最大值(self, 最大值):
        self.对象.setMaximum(最大值)

    def 置当前值(self, 当前值):
        self.对象.setValue(当前值)

    def 置方向(self, 方向):
        self.对象.setOrientation(方向)

    def 置步长(self, 步长):
        self.对象.setSingleStep(步长)

    def 置页面步长(self, 步长):
        self.对象.setPageStep(步长)



    def 绑定事件值被改变(self, 回调函数):
        """
        回调函数(int 置)
        """
        self.对象.valueChanged.connect(回调函数)
