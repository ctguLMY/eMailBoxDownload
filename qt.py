'''
Description: 
Version: 1.0
Autor: Ming
Date: 2023-12-17 22:15:28
LastEditors: Ming
LastEditTime: 2023-12-17 23:21:48
'''
import sys
from PyQt5 import QtWidgets
from download_ui import Ui_Dialog

class DownloadDialog(QtWidgets.QDialog,Ui_Dialog): #这里也要记得改
    def __init__(self,parent =None):
        super(DownloadDialog,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 初识化界面
    myDiagl = DownloadDialog()        # 生成一个主窗口
    myDiagl.show()                       # 显示主窗口
    sys.exit(app.exec_())                   # 在线程中退出  



# import sys
# from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
# from Ui_Mywin import Ui_MainWindow  #导入你写的界面类
 
 
# class MyMainWindow(QMainWindow,Ui_MainWindow): #这里也要记得改
#     def __init__(self,parent =None):
#         super(MyMainWindow,self).__init__(parent)
#         self.setupUi(self)
 
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWin = MyMainWindow()
#     myWin.show()
#     sys.exit(app.exec_())    