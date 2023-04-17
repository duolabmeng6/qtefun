
#  qtefun qt版本的中文组件库

项目地址 https://github.com/duolabmeng6/qtefun

#  [快速入门教程请点击这里查看](https://www.kancloud.cn/duolabmeng/pyefundoc/3151049)


# 组件对应的英文

| 英文 | 中文       |
| ---- |----------|
| `QtWidgets.QPushButton` | `按钮`     |
| `QtWidgets.QLabel` | `标签`     |
| `QtWidgets.QLineEdit` | `单行文本框`  |
| `QtWidgets.QPlainTextEdit` | `纯文本编辑框` |
| `QtWidgets.QTextEdit` | `富文本编辑框` |
| `QtWidgets.QCheckBox` | `复选框` |
| `QtWidgets.QRadioButton` | `单选框` |
| `QtWidgets.QListWidget` | `列表框` |
| `QtWidgets.QTreeWidget` | `树形框` |
| `QtWidgets.QTableWidget` | `表格` |
| `QtWidgets.QTabWidget` | `选择夹` |
| `QtWidgets.QTimeEdit` | `时间编辑框` |
| `QtWidgets.QDateEdit` | `日期编辑框` |
| `QtWidgets.QDateTimeEdit` | `日期时间编辑框` |
| `QtWidgets.QSpinBox` | `整数编辑框` |
| `QtWidgets.QDoubleSpinBox` | `小数编辑框` |
| `QtWidgets.QComboBox` | `组合框` |
| `QtWidgets.QFontComboBox` | `字体选择框` |
| `QtWidgets.QDial` | `圆形调节器` |
| `QtWidgets.QSlider` | `滑块条` |
| `QtWidgets.QScrollBar` | `滚动条` |
| `QtWidgets.QKeySequenceEdit` | `快捷键编辑框` |



# 加载ui文件的例子

```python
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import ui_app as ui_app #这里就是 uic生成的py文件

class 主窗口(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(415, 200)
        # 加载界面 ui_app.py
        self.ui = ui_app.Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = 主窗口()
    win.show()
    sys.exit(app.exec())

```


