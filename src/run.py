#!/usr/bin/env python3.7
# coding: utf8
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome import service as fs

url = "https://monaledge.com/mypage"
user_data_dir_path = '/home/pi/.config/chromium'
profile_dir_name = 'Profile 3'

options = webdriver.ChromeOptions()
options.add_argument(f'--user-data-dir={user_data_dir_path}')
options.add_argument(f'--profile-directory={profile_dir_name}')

chrome_service = fs.Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(options=options, service=chrome_service)
#driver.get(url)
driver.execute_script(`window.open('${url}');`)

time.sleep(30)
driver.close()
