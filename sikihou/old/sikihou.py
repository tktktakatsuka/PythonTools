
import os
# resuests モジュールをインポート
import re
import time
from tkinter import messagebox
import openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import requests
from openpyxl.utils import get_column_letter
import openpyxl
from openpyxl.styles.borders import Border, Side
import datetime

"""
isStatusCodeNomal
@param URL 取得するURL
""" 
def isStatusCodeNomal(URL):
    res = requests.get(URL)
    isStatus =  res.status_code
    print(res.status_code)
    return  isStatus
  
  
def init(path,profile):  
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=' +str(path))
    options.add_argument('--profile-directory=' +str(profile))  # この行を省略するとDefaultフォルダが指定されます
    driver = webdriver.Chrome(options = options)
    return driver
  
"""
driverOpen
@param URL 取得するURL
""" 
def driverOpen(URL):
    options = Options()
    user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36']
    options = webdriver.ChromeOptions()
    options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
    res = driver.get(URL)
      
"""
getCurrentPage
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
    
    textlist = [] 
    for item in tagList:
        textlist.append( item.getText()) 
    return textlist 

def getCurrentURLPage(className):
    #カレントページを取得する
    html =driver.page_source.encode('utf-8')
    #読み込む情報を解析する。
    soup = BeautifulSoup(html, 'html.parser') 
    #指定のクラスを リストで取得する。
    tagList = soup.select(className)
    
    urlList= []
    for item in tagList:
        url =  item.find('a')
        url = url.get('href')
        urlList.append( url)
    
    return urlList

def getgigityukiPage():
    #カレントページを取得する
    html =driver.page_source.encode('utf-8')
    #読み込む情報を解析する。
    soup = BeautifulSoup(html, 'html.parser') 
    #指定のクラスを リストで取得する。
    tagList = soup.select('//*[@id="wrapper"]/main/article/section[1]/div[2]/div[14]/p/span[2]')
    
    for item in tagList:
        url =  item.find('a').text
    return url


'''
画面遷移
'''
def moveGamen(xpath):
    elem = driver.find_element(By.XPATH,xpath)
    elem.click()   

import sqlite3
from unicodedata import name

# TEST.dbを作成する
# すでに存在していれば、それにアスセスする。
def dbAccess(dbname):
    conn = sqlite3.connect(dbname) 
    return conn


def insert_data(str銘柄,str企業名,str優待内容 ,month1 ,month2 ,必要投資金額 ,優待利回り ,配当利回り,url):

    try:
        sql = f"INSERT INTO yutai (企業名, 銘柄コード,優待内容,権利確定月①,権利確定月②,必要投資金額,優待利回り,配当利回り,URL) values (?,?,?,?,?,?,?,?,?)"     
        data = [str(str企業名),str(str銘柄),str(str優待内容),str(month1),str(month2),str(必要投資金額),str(優待利回り),str(配当利回り),url]
        cur.execute(sql, data)
        con.commit()
    except sqlite3.IntegrityError:
        global uniqueCounter
        uniqueCounter = uniqueCounter +1 
        pass
    
    
"""
mainMethod
@param void
"""
if __name__ == '__main__':
    print("処理を開始します。")
    time.sleep(2)
    
    
    #グローバル変数
    with webdriver.Chrome(ChromeDriverManager().install()) as driver:
        i = 0

        URL ="https://shikiho.toyokeizai.net/screening"
        #URLを開く
        driverOpen(URL)
        
        time.sleep(10)
