import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

form_class = uic.loadUiType("myqt_selenuim.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        
        self.driver = webdriver.Chrome('chromedriver') 
        self.driver.get('http://127.0.0.1:5000/login.html')
        self.setupUi(self)
        self.driver.find_element_by_xpath('/html/body/form/input[1]').send_keys('S00001')
        self.driver.find_element_by_xpath('/html/body/form/input[2]').send_keys('1')

        self.driver.find_element_by_xpath('/html/body/form/input[3]').click()
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('/html/body/a[3]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/table/tbody/tr[2]/td[5]/a').click()
        self.pb.clicked.connect(self.myclick)
        
        
        
    def myclick(self):
        obj_table = self.driver.find_element_by_css_selector("body > table > tbody > tr > td:nth-child(1) > table")
        obj_trs = obj_table.find_elements_by_tag_name("tr")
        for i,tr in enumerate(obj_trs):
            if i > 0 :
                print(tr.find_elements_by_tag_name("td")[0].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[1].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[2].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[3].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[4].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[5].text)
                
                

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()