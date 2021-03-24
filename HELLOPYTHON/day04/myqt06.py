import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("myqt06.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        a = self.le1.text()
        b = self.le2.text()
        int_a = int(a)
        int_b = int(b)
        arr = range(int_a,int_b+1)
        sum = 0
        for i in arr:
            sum += i
        self.le3.setText(str(sum))
        
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()