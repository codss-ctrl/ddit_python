from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import time
 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(180, 234)
 
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(40, 10, 100,50))
        self.startButton.setObjectName("startButton")
 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #startButton 클릭시 autoExcute 함수 수행
        self.startButton.clicked.connect(self.autoExcute)
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.startButton.setText(_translate("Dialog", "시작"))
 
 #셀레니움 동작 코드 함수 autoExcute 생성
    def autoExcute(self):
        driver  = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(3)
        driver.get('http://127.0.0.1:5000/login.html')
        
        driver.find_element_by_xpath('/html/body/form/input[1]').send_keys('S00001')
        driver.find_element_by_xpath('/html/body/form/input[2]').send_keys('1')

        driver.find_element_by_xpath('/html/body/form/input[3]').click()
        self.listWidget.addItem('로그인 성공')
        
        driver.find_element_by_xpath('/html/body/a[2]').click()
        driver.find_element_by_xpath('/html/body/a[3]').click()
        
        driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/table/tbody/tr[2]/td[5]/a').click()
        obj_table = driver.find_element_by_css_selector("body > table > tbody > tr > td:nth-child(1) > table")
        obj_trs = obj_table.find_elements_by_tag_name("tr")
        
        for i,tr in enumerate(obj_trs):
            if i > 0 :
                print(tr.find_elements_by_tag_name("td")[1].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[2].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[3].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[4].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[5].text)
 
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
 


