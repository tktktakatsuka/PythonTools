
import os
# resuests モジュールをインポート
from operator import truediv
import re
from bs4.builder import HTML
from openpyxl.xml.constants import ACTIVEX, XLSX
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import configparser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

"""
driversetting
@param URL 取得するURL
""" 
def driverSetting(URL):
    options = Options()
    user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36']
    options = webdriver.ChromeOptions()
    options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
    driver.get(URL)
    
"""
getCurrentPage
@param className HTMLページのクラスを指定
@return tagList
"""   
def getCurrentPage(className):
    #カレントページを取得する
    html =driver.page_source.encode('utf-8')
    #読み込む情報を解析する。
    soup = BeautifulSoup(html, 'html.parser') 
    #指定のクラスを リストで取得する。
    tagList = soup.select(className)
    mylist = []
    
    for item in tagList:
        mylist.append( item.getText())
    return mylist

"""
getItem
@param tagList HTMLのリストの中の特定のクラスを抜き出す。
@return ItemList
"""   
def getItem(tagList , tag , classname):
    mylist = []
    for item in tagList:
        '''
        アイテム変数定義
        '''
        info   = item.find(tag, class_=classname ).text     
        mylist.append(info)   
    return info 

'''
画面遷移
'''
def moveGamen():
    xpath = '//*[@id="__next"]/div[2]/div/div/div/form/button[1]'
    elem = driver.find_element(By.XPATH,xpath)
    elem.click()   
    

import sqlite3
from unicodedata import name

# TEST.dbを作成する
# すでに存在していれば、それにアスセスする。
def dbAccess(dbname):
    conn = sqlite3.connect(dbname) 
    return conn

#テーブル作成
def dbCreateTable(createSQL):
    cur.execute(createSQL)

#レコード追加
def dbInsert(insertSQL):
    cur.execute(insertSQL)
    cur.execute('INSERT INTO persons(name) values("Hanako")')
    cur.execute('INSERT INTO persons(name) values("Zirou")')
    conn.commit()

#セレクト実行
def dbSelect(selectSql):
    cur.execute(selectSql)
    print(cur.fetchall())
 
# データベースへコミット。    
def dbCommit():
    conn.commit()
 
     
# データベースへのコネクションを閉じる。(必須)    
def dbClose():
    cur.close()
    conn.close()
    


    
    

    

"""
mainMethod
@param void
"""
if __name__ == '__main__':
    
    #グローバル変数
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    #指定のURLからブラウザを開く
    URL ="https://www.kabuyutai.com/yutai/january.html"
    INI= 'properties.ini'
    driverSetting(URL)
    
    #指定のURLのクラスからデータを取得する
    className = "[class*='table_tr_info']"
    taglist = getCurrentPage(className)

    #必要な情報を取得    
    print(str(taglist[0]))
    splitedList = str(taglist[0]).splitlines
    
    #書き込みしたい文字列を表示するところまで完了
    for item in taglist:
        print(item)
    
    
    
    
    
    
    

    

    
    
    #ドライバー終了
    driver.quit()

    '''
    URLを開く
    '''

    #URLを開く

    
    
    
    
 

    
    #スクレイピング
    
    #２か月分あった場合は月を分割して入力
    
    #DBに格納
    
    #出力ファイルへ出力
    

