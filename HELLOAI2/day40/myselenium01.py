from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver') #또는 chromedriver.exe
driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 페이지 가져오기(이동)
driver.get('http://127.0.0.1:5000/login.html')


# 아이디/비밀번호를 입력해준다.
driver.find_element_by_xpath('/html/body/form/input[1]').send_keys('S00001')
driver.find_element_by_xpath('/html/body/form/input[2]').send_keys('1')


# 로그인 버튼을 누르기
driver.find_element_by_xpath('/html/body/form/input[3]').click()
driver.find_element_by_xpath('/html/body/a[2]').click()

html = driver.page_source
print("------------------------------------------")
print(html)
