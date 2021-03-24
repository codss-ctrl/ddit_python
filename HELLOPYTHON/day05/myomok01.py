import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtGui


form_class = uic.loadUiType("myomok01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.mystate = 0
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):

        if self.mystate == 0:
            self.mystate = 1
        elif self.mystate == 1:
            self.mystate = 2
        else :
            self.mystate = 0 

        pm = QtGui.QPixmap(str(self.mystate)+".png");
        self.pb.setIcon(QtGui.QIcon(pm))

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()