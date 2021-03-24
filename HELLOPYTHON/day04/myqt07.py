import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("myqt07.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        
        
    def myclick(self):
        dan = int(self.sender().text())
        text = ""
        text += ""+str(dan)+"*"+str(1)+"="+str(dan*1)+"\n"
        text += ""+str(dan)+"*"+str(2)+"="+str(dan*2)+"\n"
        text += ""+str(dan)+"*"+str(3)+"="+str(dan*3)+"\n" 
        text += ""+str(dan)+"*"+str(4)+"="+str(dan*4)+"\n"
        text += ""+str(dan)+"*"+str(5)+"="+str(dan*5)+"\n"
        text += ""+str(dan)+"*"+str(6)+"="+str(dan*6)+"\n"
        text += ""+str(dan)+"*"+str(7)+"="+str(dan*7)+"\n"
        text += ""+str(dan)+"*"+str(8)+"="+str(dan*8)+"\n"
        text += ""+str(dan)+"*"+str(9)+"="+str(dan*9)+"\n"
        
        
        self.te.setText(text)
        
        
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()