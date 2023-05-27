
import codecs

import time
from tkinter import messagebox
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import ImageGrab
import requests
import openpyxl
from openpyxl.utils import get_column_letter



"""
isStatusCodeNomal
@param URL 取得するURL
""" 
def isStatusCodeNomal(URL):
    res = requests.get(URL)
    isStatus =  res.status_code
    print(res.status_code)
    return  isStatus
  
"""
driverOpen
@param URL 取得するURL
""" 


      
"""
getCurrentTextPage
@param className HTMLページのクラスを指定
@return tagList
"""   
def getCurrentTextPage(className):
    #カレントページを取得する
    html =driver.page_source.encode('utf-8')
    #読み込む情報を解析する。
    soup = BeautifulSoup(html, 'html.parser')
    #指定のクラスを リストで取得する。
    tagList = soup.select(className)
    
    mylist = []
    with  codecs.open('file.txt', 'w' , 'utf-8') as f:
        for item in tagList:
            if item.find('div') is not None:
                    print(item.find('div').text, file=f)
    
'''
テキスト挿入
'''
def sendKey(xpath , string ):
    elem = driver.find_element(By.XPATH,xpath).send_keys(string)
    time.sleep(1)
    
'''
画面クリック
'''
def clicKey(xpath):
    elem = driver.find_element(By.XPATH,xpath)
    driver.execute_script("arguments[0].click();" , elem) 
    time.sleep(1)

def init(path,profile):  
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=' +str(path))
    options.add_argument('--profile-directory=' +str(profile))  # この行を省略するとDefaultフォルダが指定されます
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) , options = options )
    return driver
    
"""
mainMethod
@param void
"""
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    
    with webdriver.Chrome(ChromeDriverManager().install() , options= options) as driver:
        print("処理を開始します。")
        time.sleep(2)
        
        
        URL ="https://id.toyokeizai.net/sol/?return_to=%2Fscreening"
        driver.set_window_size(1280, 720)
        driver.maximize_window()
        driver.get(URL)
        time.sleep(1)

        #mailAddressを挿入
        sendKey('//*[@id="tkz_id"]' , 'tosinobu117@hotmail.com' )
        #Passwordを挿入
        sendKey('//*[@id="password"]' , 'Reij5371' )
        #loginボタンクリック
        driver.save_screenshot('screenshot_login.png')
        time.sleep(1)
        clicKey('//*[@id="mailLogin"]/div/p[1]/input')

        #保存した検索結果のダイアログクリック
        clicKey('//*[@id="pageTop"]/div[1]/div/div[2]/div/ul/li[3]/div[1]')
        driver.save_screenshot('screenshot_daialog.png')
        time.sleep(1)
        
        #対象の検索条件をクリック
        time.sleep(1)
        clicKey('//*[@id="pageTop"]/div[1]/div/div[2]/div/ul/li[3]/div[2]/ul/div[2]/div/li[26]')
        driver.save_screenshot('screenshot_reserchWord.png')
        time.sleep(1)
        
        #検索をクリック
        clicKey('//*[@id="pageTop"]/div[1]/div/div[2]/div/div/div/div/button')
        time.sleep(3)

        
        window_after = driver.window_handles[1]
        #seleniumの操作対象を当初から開いているウインドウに切り替える
        driver.switch_to.window(window_after)
        driver.save_screenshot('screenshot_result.png')
        #カレントページの取得

        #指定のURLのクラスからデータを取得する
        #className = "[class*='vgt-left-align -MIC001']"
        className = "[class*='vgt-left-align -no']"
        taglist = getCurrentTextPage(className)

        
        print('処理を終了します')