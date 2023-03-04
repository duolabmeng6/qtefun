import traceback
import datetime

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QApplication

def 异常检测(function):
    def box(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            print(function.__name__, "函数发生异常")
            print("错误发生时间：", str(datetime.datetime.now()))
            print("错误的详细情况：", traceback.format_exc())

    return box


def 加载ui文件(ui文件名,容器=None):
    from qtpy.uic import loadUi
    return loadUi(ui文件名, 容器)

def 应用退出():
    QCoreApplication.quit()

def 设置关闭窗口不退出():
    QApplication.setQuitOnLastWindowClosed(False)  # 关闭最后一个窗口不退出程序


def 置剪切板图片(图片数据: QImage):
    mimData = QtCore.QMimeData()
    mimData.setImageData(图片数据)
    QApplication.clipboard().setMimeData(mimData)



def 消息框(self, 内容="", 标题="", 类型=1, 按钮: list = None):
    """
    消息框

    :param 内容: 提示的内容
    :param 标题: 窗口的标题
    :param 类型: 1.消息框 2.错误框 3.警告框 4.问题框
    :param 按钮: 按钮的文本 参数 ["确定","取消","是","否","重试","忽略"] 如果为空则为确定按钮

    :return: 返回点击的按钮文本
    """
    if 按钮 is None:
        按钮 = ["确定"]

    按钮列表 = {
        "确定": QtWidgets.QMessageBox.Ok,
        "取消": QtWidgets.QMessageBox.Cancel,
        "是": QtWidgets.QMessageBox.Yes,
        "否": QtWidgets.QMessageBox.No,
        "重试": QtWidgets.QMessageBox.Retry,
        "忽略": QtWidgets.QMessageBox.Ignore,
    }
    # key value 互换
    按钮列表2 = {value: key for key, value in 按钮列表.items()}

    # 检查按钮的参数 循环 按钮列表 组合参数
    按钮参数 = None
    for 按钮文本 in 按钮:
        if 按钮参数 is None:
            按钮参数 = 按钮列表[按钮文本]
        else:
            按钮参数 = 按钮参数 | 按钮列表[按钮文本]

    if 类型 == 1:
        返回结果 = QtWidgets.QMessageBox.information(self, 标题, 内容, buttons=按钮参数)
    elif 类型 == 2:
        返回结果 = QtWidgets.QMessageBox.warning(self, 标题, 内容, buttons=按钮参数)
    elif 类型 == 3:
        返回结果 = QtWidgets.QMessageBox.critical(self, 标题, 内容, buttons=按钮参数)
    elif 类型 == 4:
        返回结果 = QtWidgets.QMessageBox.question(self, 标题, 内容, buttons=按钮参数)
    # print(返回结果)
    # 匹配 按钮列表 和 返回结果
    返回结果 = 按钮列表2[返回结果]
    # print(返回结果)

    return 返回结果

def 打开文件选择器(self, 文件类型: str = None, 标题="打开文件", 初始目录="."):
    """
    打开文件选择器

    :param 文件类型: 例如:  "所有文件 (*);;文本文件 (*.txt)"
    :param 标题:
    :param 初始目录: 默认当前目录
    :return: 返回选择的文件路径
    """
    if 文件类型 is None:
        文件类型 = "所有文件 (*);;文本文件 (*.txt)"
    文件路径, _ = QtWidgets.QFileDialog.getOpenFileName(self, 标题, 初始目录, 文件类型)
    return 文件路径

def 打开文件夹选择器(self, 标题="打开文件夹", 初始目录="."):
    """
    打开文件夹选择器

    :param 标题:
    :param 初始目录: 默认当前目录
    :return: 返回选择的文件夹路径
    """
    文件夹路径 = QtWidgets.QFileDialog.getExistingDirectory(self, 标题, 初始目录)
    return 文件夹路径

def 打开文件保存选择器(self, 文件类型: str = None, 标题="保存文件", 初始目录="."):
    """
    打开文件保存选择器

    :param 文件类型:  例如:  "所有文件 (*);;文本文件 (*.txt)"
    :param 标题:
    :param 初始目录:  默认当前目录
    :return: 返回选择的文件路径
    """
    文件类型 = QtWidgets.QFileDialog.getSaveFileName(self, 标题, 初始目录, 文件类型)
    return 文件类型

def 打开颜色选择器(self):
    """
    打开颜色选择器

    :return:  返回选择的颜色 例如 PySide6.QtGui.QColor.fromRgbF(0.362097, 0.190341, 0.397406, 1.000000)
    """
    color = QtWidgets.QColorDialog.getColor()
    return color

def 打开字体选择器(self):
    """
    打开字体选择器

    :return: 返回选择的字体 例如 <PySide6.QtGui.QFont(.AppleSystemUIFont,13,-1,5,400,0,0,0,0,0,0,0,0,0,0,1) at 0x12522d6c0>
    """
    _, font = QtWidgets.QFontDialog.getFont()
    return font

def 打开输入框(self, 标题="输入", 内容="请输入", 初始值="", 密码=False):
    """
    打开输入框

    :param 标题: 标题
    :param 内容: 内容
    :param 初始值: 默认为空
    :param 密码: 是否是密码框
    :return: 返回输入的值 例如 "123" , True
    """
    if 密码:
        输入结果, 确定 = QtWidgets.QInputDialog.getText(self, 标题, 内容, QtWidgets.QLineEdit.Password, 初始值)
    else:
        输入结果, 确定 = QtWidgets.QInputDialog.getText(self, 标题, 内容, QtWidgets.QLineEdit.Normal, 初始值)

    return 输入结果, 确定


import os
import sys
import socket

def 应用程序检查是否重复运行(app_name):
    """
    防止应用程序重复运行的函数。

    Parameters:
        app_name (str): 应用程序的名称。

    Returns:
        bool: 如果程序已经在运行中，则返回 True，否则返回 False。
    """
    if os.name == 'nt':
        # 如果当前操作系统是 Windows，则使用以下方式来检查程序是否已经在运行中
        import win32event
        import win32api
        import winerror
        instance_mutex = win32event.CreateMutex(None, 1, app_name)
        if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
            return True
    else:
        # 如果当前操作系统是 macOS 或 Linux，则使用以下方式来检查程序是否已经在运行中
        pidfile = f'/var/run/{app_name}.pid'
        if os.path.isfile(pidfile):
            try:
                with open(pidfile, 'r') as f:
                    pid = int(f.read().strip())
                    os.kill(pid, 0)
                    return True
            except (IOError, OSError, ValueError):
                pass
        with open(pidfile, 'w') as f:
            f.write(str(os.getpid()))
    return False