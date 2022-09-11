import requests
import bs4

class Scrapingger:
    
    """
    コンストラクタ
    file名とシート名を取得
    @ fileName = エクセルファイルパス
    @ fileName = エクセルシート名
    """
    def __init__(self,value ):  
        #カレントページを取得する
        self.res = requests.get(value).text
        #読み込む情報を解析する。
        self.soup = bs4.BeautifulSoup( self.res , 'html.parser') 


    """
    soupSelect
    指定の要素で解析
    @ pram elem 要素
    @ return elsems 要素を返す
    """
    def soupSelect(self , elem):
        elems = self.soup.select(elem)
        print(elems)
        return elems