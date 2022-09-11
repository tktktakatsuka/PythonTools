import configparser
import hmac
import time
import PySimpleGUI as sg
from h11 import Request
from requests import Request, Session
from email.mime.text import MIMEText

import requests

sg.theme('Default1')

default_args = {
    'font': ('Helvetica', 30),
}

bitbank_ask = 0
bitbank_bid = 0
bitflyer_ask = 0
bitflyer_bid = 0
BTC_JPY_ask = 0
BTC_JPY_bid = 0
USD_JPY_ask = 0
USD_JPY_bid = 0
BTC_PERP_ask = 0
BTC_PERP_bid = 0


            
down = 0

window = sg.Window(title='BitCoin Watcher').Layout(
    [
        [
            sg.Frame(


                "業者別価格",
                [                                        



                    [
                        sg.Frame(
                            "bitbank",
                            [
                                [
                                    sg.Text("bid", size=(4, 1), **default_args),
                                    sg.Text(bitbank_bid, size=(12, 1), background_color="#009fc6", key="_bitbank_bid_", **default_args),
                                    sg.Text("ask", size=(4, 1), **default_args),
                                    sg.Text(bitbank_ask, size=(12, 1), background_color="#db4d50", key="_bitbank_ask_", **default_args),
                                ]
                            ]
                        ),
                    ],

                    [
                        sg.Frame(
                            "bitFlyer",
                            [
                                [
                                    sg.Text("bid", size=(4, 1), **default_args),
                                    sg.Text(bitflyer_bid, size=(12, 1), background_color="#009fc6", key="_bitflyer_bid_", **default_args),
                                    sg.Text("ask", size=(4, 1), **default_args),
                                    sg.Text(bitflyer_ask, size=(12, 1), background_color="#db4d50", key="_bitflyer_ask_", **default_args),
                               
                                ]
                            ]
                        )
                    ],
                                        [
                        sg.Frame(
                            "FTX(BTC/PERP)",
                            [
                                [
                                    sg.Text("bid", size=(4, 1), **default_args),
                                    sg.Text(BTC_PERP_bid, size=(12, 1), background_color="#009fc6", key="_BTC_PERP_bid_", **default_args),
                                    sg.Text("ask", size=(4, 1), **default_args),
                                    sg.Text(BTC_PERP_ask, size=(12, 1), background_color="#db4d50", key="_BTC_PERP_ask_", **default_args),
                               
                                ],

                    [
                        sg.Frame(
                            "FTX(BTC/JPY)",
                            [
                                [
                                    sg.Text("bid", size=(4, 1), **default_args),
                                    sg.Text(BTC_JPY_bid, size=(12, 1), background_color="#009fc6", key="_BTC_JPY_bid_", **default_args),
                                    sg.Text("ask", size=(4, 1), **default_args),
                                    sg.Text(BTC_JPY_ask, size=(12, 1), background_color="#db4d50", key="_BTC_JPY_ask_", **default_args),
                                ]
                            ]
                        ),
                    ],

                    [
                        sg.Frame(
                            "FTX(USD/JPY)",
                            [
                                [
                                    sg.Text("bid", size=(4, 1), **default_args),
                                    sg.Text(USD_JPY_bid, size=(12, 1), background_color="#009fc6", key="_USD_JPY_bid_", **default_args),
                                    sg.Text("ask", size=(4, 1), **default_args),
                                    sg.Text(USD_JPY_ask, size=(12, 1), background_color="#db4d50", key="_USD_JPY_ask_", **default_args),
                               
                                ]
                            ]
                        )
                    ],


                            ]
                        )
                    ],

                    

                ]
            ),
        ]
    ]
)


while True:
    event, value = window.read(timeout=500, timeout_key='_timeout_')
    if event in '_timeout_':
        try:
            # ==================== 価格取得 ====================
            bitbank = requests.get('https://public.bitbank.cc/btc_jpy/ticker')
            bitbank_ask = int(bitbank.json()['data']['sell'])
            bitbank_bid = int(bitbank.json()['data']['buy'])
            window["_bitbank_ask_"].update(bitbank_ask)
            window["_bitbank_bid_"].update(bitbank_bid)

            # bitFlyer
            bitflyer = requests.get('https://api.bitflyer.com/v1/ticker?product_code=BTC_JPY')
            bitflyer_ask = int(bitflyer.json()['best_ask'])
            bitflyer_bid = int(bitflyer.json()['best_bid'])
            window["_bitflyer_ask_"].update(bitflyer_ask)
            window["_bitflyer_bid_"].update(bitflyer_bid)

            
            #config.iniより設定をする
            config_ini = configparser.ConfigParser()
            config_ini.read('config.ini', encoding='utf-8')
            APIkey = config_ini.get('DEFAULT', 'ftxkey')

            #テンプレート
            request = Request('GET', 'https://ftx.com/api/markets')
            prepared = request.prepare()
            
            
            request.headers['FTX-KEY'] = APIkey
            #データを取得してjson形式に変換する
            r = Session().send(prepared)
            rJson = r.json()
            resultKey = 'result'
    
            #jsonファイルのキーを一つずつ確認する
            for ticker in rJson[resultKey]:
                #BTC-PERP
                #ask
                if ticker['name'] == 'BTC-PERP':
                    BTC_PERP_ask =ticker['ask']
                    window["_BTC_PERP_ask_"].update(BTC_PERP_ask)
                #bid
                if ticker['name'] == 'BTC-PERP':
                    BTC_PERP_bid = ticker['bid']
                    window["_BTC_PERP_bid_"].update(BTC_PERP_bid)

                #BTC/JPY
                #ask
                if ticker['name'] == 'BTC/JPY':
                    BTC_JPY_ask =ticker['ask']
                    window["_BTC_JPY_ask_"].update(BTC_JPY_ask)
                    print(BTC_JPY_ask)
                #bid
                if ticker['name'] == 'BTC/JPY':
                    BTC_JPY_bid = ticker['bid']
                    window["_BTC_JPY_bid_"].update(BTC_JPY_bid)
                    print(BTC_JPY_bid)


                #USD_JPY
                #ask
                if ticker['name'] == 'USD/JPY':
                    BTC_JPY_bid = ticker['ask']
                    window["_USD_JPY_ask_"].update(BTC_JPY_bid)
                    print(BTC_JPY_bid)
                #bid
                if ticker['name'] == 'USD/JPY':
                    BTC_JPY_bid = ticker['bid']
                    window["_USD_JPY_bid_"].update(BTC_JPY_bid)
                    print(BTC_JPY_bid)
                    


        except Exception as e:
            print(e)