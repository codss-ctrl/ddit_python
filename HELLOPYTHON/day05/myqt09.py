import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("myqt09.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        mine = self.le_mine.text()
        com = ""
        result = ""
        
        rnd = random.random()
        if rnd > 0.66:
            com = "가위"
        elif rnd > 0.33:
            com = "바위"    
        else:
            com = "보"  
 
        if com == "가위" and mine == "가위"  :
            result = "비김"
        elif com == "가위" and mine == "바위"  :
            result = "이김"
        elif com == "가위" and mine == "보"  :
            result = "짐"
            
        elif com == "바위" and mine == "가위"  :
            result = "짐"
        elif com == "바위" and mine == "바위"  :
            result = "비김"
        elif com == "바위" and mine == "보"  :
            result = "이김"
            
        elif com == "보" and mine == "가위"  :
            result = "이김"
        elif com == "보" and mine == "바위"  :
            result = "보"
        elif com == "보" and mine == "보"  :
            result = "짐"
         
        self.le_com.setText(com)
        self.le_result.setText(result)


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()