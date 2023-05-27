
import os
# resuests モジュールをインポート
import re
import sqlite3
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
    tagList = soup.select("[class*=table_tr]")
    urlList = []
    
    for item in tagList:

        url =  item.find('p').text
        urlList.append( url)
    print(urlList)
    return url


'''
画面遷移
'''
def moveGamen(xpath):
    elem = driver.find_element(By.XPATH,xpath)
    elem.click()   

"""
mainMethod
@param void
"""
if __name__ == '__main__':
    

    #グローバル変数
    with webdriver.Chrome(ChromeDriverManager().install()) as driver:
        i = 0
    
    
        con = sqlite3.connect('yuutai.sqlite3')
        cur = con.cursor()
        cur.execute('create table IF NOT EXISTS yutai(企業名 , 銘柄コード unique , 優待内容  , 権利確定月① , 権利確定月② , 必要投資金額  , 優待利回り , 配当利回り,URL )')
        uniqueCounter = 0
        
        MONTHList = ["january", 
                     "february" ,
                     "march" ,
                     "april" ,
                     "may" , 
                     "june" ,
                     "july" ,
                     "august" , 
                     "september" , 
                     "october" ,
                     "november" , 
                     "december"  ]

        for mList in MONTHList:
            
            while(True):
                time.sleep(1)

                URL ="https://www.kabuyutai.com/yutai/march.html"

                #ページがなかったら処理終了
                if(isStatusCodeNomal(URL) == 404):
                    i=0
                    break
                
                #URLを開く
                driverOpen(URL)

                #指定のURLのクラスからデータを取得する
                className = "[class*='table_tr_info']"
                taglist = getCurrentTextPage(className)
                
                url = getgigityukiPage()
                print("疑義中期取得   " +'【'+ url +'】')
                
                urllist = getCurrentURLPage(className)

                coutner = 0
                #書き込みしたい文字列を表示するところまで完了
                for item in taglist:
                    
                    url = urllist[coutner]

                    #必要な情報を取得    
                    splitedList = str(item).splitlines()
                    
                    #infoがあった場合に削除するためのif分
                    if '長期優待を狙えば、' in splitedList[2]:
                        splitedList.pop(2) #これでインデックス番号2番の削除後詰める
                    #長期優待を削除するためのif分
                    for item in taglist:
                        
                        if '【長期優待】' in splitedList[2]:
                            splitedList.pop(2) #これでインデックス番号2番の削除後詰める
                        
                        if '【長期優待】' in splitedList[3]:
                            splitedList.pop(3) #これでインデックス番号2番の削除後詰める