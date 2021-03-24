from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import sys

# 인터넷 익스플로러 드라이버 위치
driver = webdriver.Ie('')
print("프로그램 실행중....")

#driver = webdriver.Edge("‪E:\\python\\edgedriver_win64\\msedgedriver.exe")

driver.implicitly_wait(3)
driver.set_window_size(1280, 720)
driver.get('http://df.nexon.com/')


try:    # 던파 이벤트 페이지로 시작할시
    nx_login = driver.find_element_by_class_name("login_btn")
    nx_login.click()
except NoSuchElementException:  # 던파 메인 홈페이지로 시작할시
    btn_nx = driver.find_element_by_class_name("btn_nx")
    btn_nx.click()
finally:
    nx_id = driver.find_element_by_id('txtNexonID')
    nx_pw = driver.find_element_by_id('txtPWD')
    nx_sumbit = driver.find_element_by_id('btnLogin')

while driver.get:
    nx_id.clear()
    # 넥슨 아이디
    nx_id.send_keys("")

    nx_pw.clear()
    # 넥슨 비밀번호
    nx_pw.send_keys("")

    nx_sumbit.click()
    break


try:    # 던파 이벤트 페이지로 바로 시작하면 실행
    gamestart = driver.find_element_by_id('tmGameStart')
    gamestart.click()
except NoSuchElementException:  # 던파 메인 홈페이지로 시작할시
    gameStartSp = driver.find_element_by_id('gameStartSp')
    gameStartSp.click()
except TimeoutException:
    driver.close()
    driver.quit()
    print("프로그램 실행 완료")
    print("프로그램을 종료합니다...")
