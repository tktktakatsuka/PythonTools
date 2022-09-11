

import configparser
from fileinput import filename
from logging import exception
import os
import time
import traceback
from urllib import request
from ChromeDriver import ChromeDriver
from ExcelOperator import ExcelOperator


"""
main関数
"""
if __name__ == '__main__':

    try:

        print('処理を開始します。')

        """
        driversetting
        """
        config_ini = configparser.ConfigParser()
        config_ini.read('config.ini', encoding='utf-8')
        read_default = config_ini['DEFAULT']

        var1 = read_default.get('profilePath')
        print(var1)
        var2 = read_default.get('profileFolder')
        print(var2)
        time.sleep(1)

        #エクセルインスタンス呼び出し
        retu = 1
        gyou = 2
        exceloperator = ExcelOperator('count.xlsx')

        #クロムドライバークラスを代入
        chromedriver = ChromeDriver(var1,var2)

        #値読み込み(max行分繰り返し作業を実施する。)
        for i in range(1, exceloperator.getRow()):



            #指定のセルに書き込んだURLをvalueへ格納する。
            value = exceloperator.loadValue(gyou , retu)
            print(value)

            #指定のURLにアクセスする
            chromedriver.urlAccess(value)

            #URLを引数にして解析する。
            scrapingger   = chromedriver.parse('body')


            #bodyタグを引数にして、指定の要素の値を代入
            elems = chromedriver.parse('body')

            #要素のテキストを取得する
            elemText = elems[0].text.replace(' ', '').replace('　', '')
            print(elemText)


            #改行で分割
            listt = elemText.splitlines()
            print(listt)
            converted   = set(listt)
            StringCounter = 0


            #書き込み処理
            f = open('.//output//myfile' + str(i) +'.txt', 'w', encoding='utf-8')
            for item in converted: 
                mozisuu = len(item)
                StringCounter = StringCounter + mozisuu
                f.write( str(item) + '\n')        
            f.close()    

            #文字サイズ出力と値をエクセルに書き込み
            print( str(StringCounter) + '文字です')
            exceloperator.writeValue(StringCounter , gyou , 2)
            #行をインクリメントする
            gyou = gyou + 1

        print('処理を終了します。')
        input()
    #例外発生時に
    except exception:
        print('例外発生')
        traceback.print_exc()
        input()