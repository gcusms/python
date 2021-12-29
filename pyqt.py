import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QGroupBox, QTabWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QCoreApplication


# BOX1的加载
def Box1():
    box1 = QGroupBox()
    box1.setFixedHeight(100)
    btn1 = QPushButton('按钮1')
    btn2 = QPushButton('按钮2')
    btn3 = QPushButton('退出')
    btn1.clicked.connect(lambda: print(btn1.text()))  # connect button
    btn3.clicked.connect(QCoreApplication.instance().quit)  # 关闭程序

    layouth = QHBoxLayout()
    layouth.addWidget(btn1)
    layouth.addWidget(btn2)
    layouth.addWidget(btn3)
    box1.setLayout(layouth)
    return box1


# BOX2的加载
def Box2():
    box1 = QGroupBox()
    table_widget = QTabWidget()
    table_widget.setWindowTitle('选项卡')

    win1 = Win1()
    win2 = Win2()
    table_widget.addTab(win1, '选项1')
    table_widget.addTab(win2, '选项2')

    layout_h = QHBoxLayout()
    layout_h.addWidget(table_widget)
    box1.setLayout(layout_h)
    return box1


class Win1(QWidget):
    def __init__(self, parent=None):
        super(Win1, self).__init__(parent)   # 解决多重继承的问题
        self.setStyleSheet('background-color: rgb(250,250,200)')
        self.btn_1 = QPushButton('打开')
        self.btn_2 = QPushButton('关闭')

        # 垂直控件
        layout_main = QVBoxLayout()
        layout_main.addWidget(self.btn_1)
        layout_main.addWidget(self.btn_2)
        self.setLayout(layout_main)


class Win2(QWidget):
    def __init__(self, parent=None):
        super(Win2, self).__init__(parent)   # 解决多重继承的问题
        self.btn_1 = QPushButton('button1')
        self.btn_2 = QPushButton('button2')
        self.btn_3 = QPushButton('button3')
        # 垂直控件
        layout_main = QVBoxLayout()
        layout_main.addWidget(self.btn_1)
        layout_main.addWidget(self.btn_2)
        layout_main.addWidget(self.btn_3)
        self.setLayout(layout_main)


class WindowClass(QWidget):
    def __init__(self, parent=None):
        super(WindowClass, self).__init__(parent)   # 解决多重继承的问题
        # self.btn1 = QPushButton('按钮1')
        # self.btn1.clicked.connect(lambda: print(self.btn1.text()))  # connect button
        # 水平控件
        self.box1 = Box1()
        self.box2 = Box2()
        layout_main = QVBoxLayout()
        layout_main.addWidget(self.box1)
        layout_main.addWidget(self.box2)
        self.setLayout(layout_main)


if __name__ == '__main__':
    # 获得命令行参数
    app = QApplication(sys.argv)
    # 声明对象
    win = WindowClass()

    # 设置窗口的名称
    win.setWindowTitle('你好python123')
    # 设置窗口的大小
    win.setFixedSize(640, 480)
    # 显示窗口
    win.show()
    # 程序运行
    sys.exit(app.exec())
