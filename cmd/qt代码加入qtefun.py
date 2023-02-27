from pyefun import *
from pyefun.调试 import *


def 将qt的ui代码加入qtefun(代码文件内容):
    # 代码文件内容 = 读入文本("ui_app.py")
    组件中英文对照 = {
        # "主窗口": "QMainWindow",
        "按钮": "QPushButton",
        "标签": "QLabel",
        "单行编辑框": "QLineEdit",
        "纯文本编辑框": "QPlainTextEdit",
        "富文本编辑框": "QTextEdit",
        "复选框": "QCheckBox",
        "单选框": "QRadioButton",
        "列表框": "QListWidget",
        "树形框": "QTreeWidget",
        "表格": "QTableWidget",
        "选择夹": "QTabWidget",
        # "容器": "QWidget",
        "时间编辑框": "QTimeEdit",
        "日期编辑框": "QDateEdit",
        "日期时间编辑框": "QDateTimeEdit",
        "整数编辑框": "QSpinBox",
        "小数编辑框": "QDoubleSpinBox",
        "组合框": "QComboBox",
        "字体选择框": "QFontComboBox",
        "圆形调节器": "QDial",
        "滑块条": "QSlider",
        "滚动条": "QScrollBar",
    }
    # 取所有key的value
    英文的key = list(组件中英文对照.values())

    # 互换键值对并且加入
    def 取组件名称中英文对照(名称):
        vv = 组件中英文对照.copy()
        vv.update({v: k for k, v in vv.items()})
        name = vv.get(名称, False)
        return name

    # 一行一行的读入代码

    依赖列表 = []
    注入代码列表 = []
    所有的代码 = 分割文本(代码文件内容, "\n")
    for i, 一行代码 in enumerate(所有的代码):
        if 判断文本(一行代码, ["="]) == False:
            continue
        找到了 = False
        for v in 英文的key:
            组件对象代码 = f"= {v}("
            # print(组件对象代码)
            if 判断文本(一行代码, [组件对象代码]):
                找到了 = True
                break
        if 找到了 == False:
            continue
        # ic(一行代码, v)
        # 修改代码
        中文组件名称 = 取组件名称中英文对照(v)
        # ic(中文组件名称)
        依赖列表.append(中文组件名称)

        变量名 = 一行代码.split("=")[0].strip()
        # 替换掉 self.
        变量名 = 变量名.replace("self.", "")
        # ic(变量名, 中文组件名称)
        全新变量名 = strCut(变量名, "_$")
        # ic(全新变量名)
        if 全新变量名 != "":
            全新变量名 = 中文组件名称 + "_" + 全新变量名
        else:
            全新变量名 = 中文组件名称

        注入代码 = f"self.{全新变量名} = {中文组件名称}(self.{变量名})"
        # ic(注入代码)

        注入代码列表.append(注入代码)

    # 依赖列表的去重
    依赖列表 = list(set(依赖列表))
    # ic(依赖列表)
    # 将依赖列表的组合起来
    依赖代码 = "\n".join([f"from qtefun.组件.{i} import {i}" for i in 依赖列表])
    # ic(依赖代码)
    代码文件内容 = 代码文件内容.replace("class Ui_MainWindow(object):", f"{依赖代码}\nclass Ui_MainWindow(object):")
    代码文件内容 = 代码文件内容.replace("# retranslateUi", "# retranslateUi \n        " + "\n        ".join(注入代码列表))
    return 代码文件内容


import sys
import subprocess



def 调用uic生成代码(uic文件路径, ui文件路径, 保存文件路径):
    # 调用 pyside6-uic.exe app.ui -o ui_app.py

    subprocess.call(f"{uic文件路径} {ui文件路径} -o {保存文件路径}", shell=True)

# 在终端输出日志
import logging

# 制作为命令 接收参数 ui代码文件 保存文件路径
if __name__ == '__main__':
    # 在pycharm中设置外部工具
    # 名字 Pyside6-UIC2Qtefun
    # 程序 python
    # 实参 C:\pyefun\QtEsayDesigner\qtefun\cmd\qt代码加入qtefun.py $FileName$ ui_$FileNameWithoutExtension$.py pyside6-uic.exe
    # 工作目录 $FileDir$
    # 在终端运行下面的命令 即可自动监控界面的更新
    # python \qtefun\cmd\qt代码加入qtefun.py app.ui ui_app.py "C:\Users\你的用户名\Anaconda3\Scripts\pyside6-uic.exe"
    uic文件路径 = None
    try:
        ui文件路径 = sys.argv[1]
        保存文件路径 = sys.argv[2]
        uic文件路径 = sys.argv[3]
    except:
        pass
        # print("参数错误")

    if uic文件路径 is None:
        uic文件路径 = "pyside6-uic.exe"

    print("uic path", uic文件路径)
    print("ui path", ui文件路径)
    print("save path", 保存文件路径)
    # 获取自身python路径
    # python路径 = sys.executable
    # print("python path", python路径)

    调用uic生成代码(uic文件路径, ui文件路径, 保存文件路径)

    代码文件内容 = 读入文本(保存文件路径)
    if not 代码文件内容:
        print("可能未安装 pysidex6-uic 未能成功生成代码")
        exit()
    代码文件内容 = 将qt的ui代码加入qtefun(代码文件内容)
    # 写到文件(保存文件路径+"_test.py", 代码文件内容)
    写到文件(保存文件路径, 代码文件内容)
    # exit()

    # 检查ui文件路径的文件是否内容被变更
    修改时间 = int(文件_获取文件信息(ui文件路径)[1])
    修改时间_上次 = 修改时间
    while True:
        # 5秒检查一次差不多了 基本跟实时的一样
        延时(5)
        try:
            修改时间 = int(文件_获取文件信息(ui文件路径)[1])
            # logging.error("check"+str(修改时间))
            # 如果修改时间不一样
            if 修改时间 != 修改时间_上次:
                logging.error("Output interface file")
                修改时间_上次 = 修改时间
                调用uic生成代码(uic文件路径, ui文件路径, 保存文件路径)
                代码文件内容 = 读入文本(保存文件路径)
                代码文件内容 = 将qt的ui代码加入qtefun(代码文件内容)
                写到文件(保存文件路径, 代码文件内容)
        except:
            pass
            exit(0)
