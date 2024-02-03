
import os
import time
import Reserch

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.common.utils import keys_to_typing
from script import *
import random
import configparser




"""フィールドを定義する
"""
config_ini = configparser.ConfigParser()
base = os.path.dirname(os.path.abspath(__file__))

#config.iniより設定をする
config_ini.read('config.ini', encoding='utf-8')
var2 = config_ini.get('DEFAULT', 'Driverpath')
var3 = config_ini.get('DEFAULT', 'InputWb')
var4 = config_ini.get('DEFAULT', 'Option')
var5 = config_ini.get('DEFAULT', 'WaitTime')


user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
                  ]
options = webdriver.ChromeOptions()
options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
options.add_argument(var4)
driver = webdriver.Chromedriver = webdriver.Chrome( ChromeDriverManager().install() , chrome_options=options )
"""メインメソッドを定義
"""
if __name__ == "__main__":
    
    driver.get('https://jmty.jp/users/sign_in')
    
# 入力フォームに値をセット
email = driver.find_element('id' , 'user_email')
time.sleep(3)
email.send_keys('test')

print("処理を終了します。")