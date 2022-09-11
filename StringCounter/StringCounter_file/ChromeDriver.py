from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import chromedriver_binary
from bs4 import BeautifulSoup

class ChromeDriver:
    
    """
    コンストラクタ
    file名とシート名を取得
    @ fileName = エクセルファイルパス
    @ fileName = エクセルシート名
    """
    def __init__(self,path,profile):  
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=' +str(path))
        self.options.add_argument('--profile-directory=' +str(profile))  # この行を省略するとDefaultフォルダが指定されます
        self.driver = webdriver.Chrome(options = self.options)


    """
    urlAccess
    file名とシート名を取得
    @ URL = アクセスするURL
    """
    def urlAccess(self,URL):       
        self.driver.get(URL)
        time.sleep(2)


    """
    parse
    現在のページを解析して、リストで返却する。
    @ tag = タグ
    """
    def parse(self , tag):
        '''
        soupに解析させる
        '''
        #カレントページを取得する
        html =self.driver.page_source.encode('utf-8')
        #読み込む情報を解析する。
        soup = BeautifulSoup(html, 'html.parser') 
        #指定のクラスを リストで取得する。
        taglist = soup.select(tag)
        return taglist
