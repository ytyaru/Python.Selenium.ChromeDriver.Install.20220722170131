#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By

url = "https://monaledge.com/mypage"
user_data_dir_path = '/home/pi/.config/chromium'
profile_dir_name = 'Profile 3'

options = webdriver.ChromeOptions()
options.add_argument(f'--user-data-dir={user_data_dir_path}')
options.add_argument(f'--profile-directory={profile_dir_name}')

chrome_service = fs.Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(options=options, service=chrome_service)
#driver.get(url)
driver.execute_script(f"window.open('{url}');")

#time.sleep(30)
#driver.close()

time.sleep(30)

def yet_login():
    #driver.execute_script(f"window.open('{url}');")
    #print(driver.find_element(By.CSS_SELECTOR, "title"))
    #print(len(driver.find_elements(By.CSS_SELECTOR, "a")))
    #elements = driver.find_elements(By.CSS_SELECTOR, "a[href^='/article/']")
    #username = driver.find_element(By.CSS_SELECTOR, "div.v-card__title.display-1.text--primary").text
    username = driver.find_element(By.CSS_SELECTOR, "div.display-1").text
    print('username:', username)
    elements = driver.find_elements(By.CSS_SELECTOR, "a")
    #elements.filter(lambda x: x.get_attribute('href').startswith('/article/'))
    #list(map(lambda e: e.get_attribute('href')))
    urls = list(map(lambda e: e.get_attribute('href'), elements))
    print(len(urls), urls)
    elements = list(filter(lambda x: x.startswith('/article/'), urls))
    print(len(elements))
    if 0 < len(elements): return False
    return True

while yet_login():
    time.sleep(3)

print('ログイン済みであることを確認しました！')

# クリックボタンを押す
#browser.find_elements_by_css_selector("header button")[-1].click()
