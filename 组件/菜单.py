from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu


class 菜单(QMenu):
    菜单项列表 = {}  # type:@QAction
    parent = None

    def __init__(self, parent=None, 标题=None, 对象名称=None):
        super().__init__(parent)
        self.parent = parent
        if 标题:
            self.设置标题(标题)

        if 对象名称:
            self.设置对象名称(对象名称)
        self.菜单项列表 = {}

    def 设置对象名称(self, 对象名称):
        self.setObjectName(对象名称)

    def 设置标题(self, 标题):
        self.setTitle(标题)

    def 取菜单项目对象(self, 菜单名):
        return self.菜单项列表[菜单名]  # type: QAction

    def 添加项目(self, 名字, 图标=None, 回调函数=None, 快捷键=None, 选中状态=None):
        菜单项 = QAction(名字, self.parent)
        if 图标:
            菜单项.setIcon(图标)
        if 快捷键:
            菜单项.setShortcut(快捷键)
        if 回调函数:
            菜单项.triggered.connect(回调函数)
        if 选中状态 is not None:
            菜单项.setCheckable(True)
            菜单项.setChecked(选中状态)

        self.菜单项列表[名字] = 菜单项
        self.addAction(菜单项)
        return 菜单项

    def 添加分隔条(self):
        self.addSeparator()

    def 取菜单项目(self):
        return self.menuAction()

    def 设置项目是否选中(self, 名字, 是否选中):
        print("设置项目是否选中", self.菜单项列表.get(名字))
        if self.菜单项列表.get(名字):
            self.菜单项列表[名字].setCheckable(True)
            self.菜单项列表[名字].setChecked(是否选中)

    def 取项目选中状态(self, 名字):
        return self.菜单项列表[名字].isChecked()
