import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QGroupBox, QLineEdit, QFileDialog, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QCoreApplication
import cv2


# BOX1的加载
class Box1(QWidget):
    def __init__(self, parent=None):
        super(Box1, self).__init__(parent)  # 解决多重继承的问题
        self.box1 = QGroupBox()
        self.box1.setFixedHeight(100)
        self.btn1 = QPushButton('加载图像路径')
        self.btn2 = QPushButton('格式化')
        self.btn_save = QPushButton('加载保存路径')
        self.btn3 = QPushButton('退出')
        self.btn1.clicked.connect(lambda: print(self.btn1.text()))  # connect button
        self.btn3.clicked.connect(QCoreApplication.instance().quit)  # 关闭程序
        self.layouth = QHBoxLayout()
        self.layouth.addWidget(self.btn1)
        self.layouth.addWidget(self.btn_save)
        self.layouth.addWidget(self.btn2)
        self.layouth.addWidget(self.btn3)
        self.box1.setLayout(self.layouth)


# BOX2的加载
class Box2(QWidget):
    def __init__(self, parent=None):
        super(Box2, self).__init__(parent)  # 解决多重继承的问题
        self.box2 = QGroupBox()
        self.text1 = QLineEdit()
        self.text1.setPlaceholderText('读取图片文件夹路径')
        self.text1_save = QLineEdit()
        self.text1_save.setPlaceholderText('保存图片文件夹路径')
        self.text2 = QLineEdit()
        self.text2.setPlaceholderText('长')
        self.text3 = QLineEdit()
        self.text3.setPlaceholderText('宽')
        self.layout_h = QHBoxLayout()
        self.layout_h.addWidget(self.text1)
        self.layout_h.addWidget(self.text1_save)
        self.layout_h.setStretch(0, 1)
        self.layout_h.addWidget(self.text2)
        self.layout_h.addWidget(self.text3)
        self.box2.setLayout(self.layout_h)


class WindowClass(QWidget):
    def __init__(self, parent=None):
        super(WindowClass, self).__init__(parent)  # 解决多重继承的问题
        # self.btn1 = QPushButton('按钮1')
        # self.btn1.clicked.connect(lambda: print(self.btn1.text()))  # connect button
        # 水平控件
        self.box1_cla = Box1()  # 对象1声明
        self.box1_cla.btn1.clicked.connect(lambda: self.Dir_read())
        self.box1_cla.btn2.clicked.connect(lambda: self.Image_Char())
        self.box1_cla.btn_save.clicked.connect(lambda: self.SaveDir())
        self.box2_cla = Box2()  # 对象2声明
        layout_main = QVBoxLayout()
        layout_main.addWidget(self.box1_cla.box1)
        layout_main.addWidget(self.box2_cla.box2)
        self.setLayout(layout_main)


    def Image_Char(self):
        flag_path = self.box2_cla.text1.text() + self.box2_cla.text1_save.text()
        flag_size = self.box2_cla.text2.text() + self.box2_cla.text2.text()
        if len(flag_path) != 0 and len(flag_size) != 0:
            s = self.box2_cla.text1.text() + '\n' + self.box2_cla.text2.text() + ' ' + self.box2_cla.text2.text()
            print(s)
            path_input = self.box2_cla.text1.text()  # 加载图片文件夹
            list_path = os.listdir(path_input)
            for filename in list_path:
                src_img_ = cv2.imread(path_input + '/' + filename)
                print(filename)
                write_img = cv2.resize(src_img_, (int(self.box2_cla.text2.text()), int(self.box2_cla.text3.text())))
                cv2.imwrite(str(self.save_path_sub) + '/' + filename, write_img)
                # if filename == list_path[]:
                #     break
            print('Image Save Successful')

        else:
            message = QMessageBox
            message = QMessageBox.information(self, "注意", "请判断路径是否正确\n或大小是否已经设置", QMessageBox.Yes | QMessageBox.No)  # 使用infomation信息框"标题

    def SaveDir(self):
        self.save_path_sub = QFileDialog.getExistingDirectory(self)  # 文件保存路径
        self.box2_cla.text1_save.setText(self.save_path_sub)

        # img = cv2.imread('D:/tu/in/squire.jpeg')
        # cv2.imshow('image', img)
        # write_img = cv2.resize(img, (640,480))
        # cv2.imwrite('D:/tu/in/img/2.jpg', write_img)
        # cv2.waitKey(0)

    def Dir_read(self):
        download_path = QFileDialog.getExistingDirectory(self)
        self.box2_cla.text1.setText(download_path)


if __name__ == '__main__':
    # 获得命令行参数
    app = QApplication(sys.argv)
    # 声明对象
    win = WindowClass()
    # 设置窗口的名称
    win.setWindowTitle('图片格式化程序')
    # 设置窗口的大小
    win.setFixedSize(640, 480)
    # 显示窗口
    win.show()
    # 程序运行
    sys.exit(app.exec())
