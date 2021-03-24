from selenium import webdriver

driver = webdriver.Ie('')

driver.implicitly_wait(3)
driver.set_window_size(1280, 720)
driver.get('http://tos.nexon.com/')

nx_login = driver.find_element_by_class_name("login_btn")
nx_login.click()

nx_id = driver.find_element_by_id('txtNexonID')
nx_pw = driver.find_element_by_id('txtPWD')
nx_submit = driver.find_element_by_id('btnLogin')

while driver.get:
    nx_id.clear()
    nx_id.send_keys("")
    
    nx_pw.clear()
    nx_pw.send_keys("")
    
    nx_submit.click()
    break
gamestart = driver.find_element_by_id('tmGameStart')
gamestart.click()
driver.close()
driver.quit()