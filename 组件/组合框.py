from PySide6 import QtWidgets

from qtefun.组件.组件公共类 import 组件公共类


# https://doc.qt.io/qt-6/qcombobox.html
# 组合框 添加项目 删除项目 取项目数量 取项目文本 取项目索引 取当前选中项目索引 取当前选中项目文本
# 事件
# void	activated(int index) # 项目被点击时触发
# void	currentIndexChanged(int index) # 当前选中项目索引改变时触发
# void	currentTextChanged(const QString &text) # 当前选中项目改变时触发
# void	editTextChanged(const QString &text) # 编辑文本改变时触发
# void	highlighted(int index) # 项目被点击时触发
# void	textActivated(const QString &text) # 项目被点击时触发
# void	textHighlighted(const QString &text) # 项目被点击时触发

class 组合框(组件公共类):
    对象 = None  # type: QtWidgets.QComboBox
    # 获取标题
    @property
    def 内容(self):
        return self.对象.currentText()

    # 获取和设置属性 现行选中项
    @property
    def 现行选中项(self):
        return self.取选中项目索引()

    @现行选中项.setter
    def 现行选中项(self, 索引: int):
        return self.设置选中项目索引(索引)


    # 添加项目
    def 添加项目(self, 文本: str):
        return self.对象.addItem(文本)

    # 删除项目
    def 删除项目(self, 索引: int):
        return self.对象.removeItem(索引)

    # 插入项目
    def 插入项目(self, 索引: int, 文本: str):
        return self.对象.insertItem(索引, 文本)

    # 取项目数量
    def 取项目数量(self):
        return self.对象.count()

    # 取项目文本
    def 取项目文本(self, 索引: int):
        return self.对象.itemText(索引)

    # 取项目索引
    def 取项目索引(self, 文本: str):
        for i in range(self.对象.count()):
            if self.对象.itemText(i) == 文本:
                return i
        return -1

    # 取选中项目索引
    def 取选中项目索引(self):
        return self.对象.currentIndex()

    # 设置选中项目索引
    def 设置选中项目索引(self, 索引: int):
        return self.对象.setCurrentIndex(索引)



    def 绑定事件项目被点击(self, 回调函数):
        """
        回调函数(int 索引)
        """
        self.对象.activated.connect(回调函数)

    def 绑定事件当前选中项目索引改变(self, 回调函数):
        """
        回调函数(int 索引)
        """
        self.对象.currentIndexChanged.connect(回调函数)

    def 绑定事件当前选中项目改变(self, 回调函数):
        """
        回调函数(str 文本)
        """
        self.对象.currentTextChanged.connect(回调函数)

    def 绑定事件编辑文本改变(self, 回调函数):
        """
        回调函数(str 文本)
        """
        self.对象.editTextChanged.connect(回调函数)

    def 绑定事件项目选中(self, 回调函数):
        """
        回调函数(int 索引)
        """
        self.对象.highlighted.connect(回调函数)

    def 绑定事件项目选中文本(self, 回调函数):
        """
        回调函数(str 文本)
        """
        self.对象.textActivated.connect(回调函数)

    def 绑定事件项目选中高亮文本(self, 回调函数):
        """
        回调函数(str 文本)
        """
        self.对象.textHighlighted.connect(回调函数)





