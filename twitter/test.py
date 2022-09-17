
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import tkinter as tk
import tkinter.ttk as ttk


def csvGrep():
       # テスト
    #データフレームを配列にして返却
    tweets_df = df_read()
    #表示させる列を選択する。
    greped_df = tweets_df[["Tweet text", "time","impressions","likes", "retweets", "replies" , "engagements" , "url clicks"]]

    #指定のカラムで降順で表示させる
    sorted_df = greped_df.sort_values('engagements', ascending=False)

    #データフレーム追加（titleのみ）
    sorted_df['記事内のアフィリエイトリンクのクリック率']    = ''
    sorted_df['気をつけた事']                             = ''
    sorted_df['発生金額']                                 = ''

    #指定の範囲の時間で抽出する
    sorted_df["time"] = pd.to_datetime(sorted_df['time'] )
    sorted_df["time"] = sorted_df['time'].dt.strftime('%Y-%m-%d ')
    sorted_df["time"] = pd.to_datetime(sorted_df['time'])
    print(sorted_df.dtypes)
    #sorted_df = sorted_df.set_index('time')
    result_df =sorted_df[(sorted_df['time'] >= dt.datetime(2022,7,3)) & (sorted_df['time'] < dt.datetime(2022,9,6))]
    #エクセルへ出力する。
    result_df.to_excel ('out.xlsx',encoding='cp932')
    print(result_df)

def df_read():
    #TweetのデータをDataFrameに格納
    df_June      = pd.read_csv("06.csv")
    df_july      = pd.read_csv("07.csv")
    df_augast    = pd.read_csv("08.csv")
    df_september = pd.read_csv("09.csv")
    combine = [ df_july , df_augast, df_september , df_June ]
    print(df_july.columns.values)
    tweets_df = pd.concat(combine)
    return tweets_df   

# rootメインウィンドウの設定
root = tk.Tk()
root.title("twitter情報抽出ツール")
root.geometry("600x450")

'''
flameの定義
'''
frame1 = tk.Frame(root, pady=10, padx=10)
frame2 = tk.Frame(root, pady=10, padx=10)
frame3 = tk.Frame(root, pady=10, padx=10)

frame1.pack()
frame2.pack()
frame3.pack()

'''
wigetの定義
'''
CsvFile    = tk.Label(frame1, text='①結合するCSVファイルの名を3つまで記入してください' , anchor='w' )
entry1     = tk.Entry(frame1)
entry2     = tk.Entry(frame1)
entry3     = tk.Entry(frame1)




grepPeriod    = tk.Label(frame2, text='②抽出期間を指定してください。※例:hogehoge.csv', anchor='w' )

labelYear1    = tk.Label(frame2, text='年')
labelMonth1   = tk.Label(frame2, text='月')
labelDay1     = tk.Label(frame2, text='日')
labelBetween  = tk.Label(frame2, text='～')
labelYear2    = tk.Label(frame2, text='年')
labelMonth2   = tk.Label(frame2, text='月')
labelDay2     = tk.Label(frame2, text='日')



#コンボボックス
module = ('2020', '2021', '2022', '2023', '2024', '2025')
combobox1 = ttk.Combobox(frame2,values=module , height = 2, width = 6)
module = ('1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12')
combobox2 = ttk.Combobox(frame2,values=module , height = 2, width = 3)
module = ('1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12','13', '14', '15', '16', '17', '18','19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30','31')
combobox3 = ttk.Combobox(frame2,values=module , height = 2, width = 3)
module = ('2020', '2021', '2022', '2023', '2024', '2025')
combobox4 = ttk.Combobox(frame2,values=module ,height = 2, width = 6)
module = ('1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12')
combobox5 = ttk.Combobox(frame2,values=module , height = 2, width = 3)
module = ('1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12','13', '14', '15', '16', '17', '18','19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30','31')
combobox6 = ttk.Combobox(frame2,values=module ,height = 2, width = 3)



button1 = ttk.Button(frame3 , text='OK.'    ,command=csvGrep)
button2 = ttk.Button(frame3 , text='Cancel.',command="")





'''
画面を配置する処理
'''
CsvFile.pack(fill = 'x', padx=2, side = 'top',pady=20)
entry1.pack(fill = 'x', padx=5, side = 'left',pady=20)
entry2.pack(fill = 'x', padx=5, side = 'left',pady=20)
entry3.pack(fill = 'x', padx=5, side = 'left',pady=20,)

grepPeriod.pack (fill = 'x', padx=2, side = 'top',pady=20)
combobox1.pack  (fill = 'x', padx=2, side = 'left',pady=20)
labelYear1.pack (fill = 'x', padx=2, side = 'left',pady=20)
combobox2.pack  (fill = 'x', padx=2, side = 'left',pady=20)
labelMonth1.pack(fill = 'x', padx=2, side = 'left',pady=20)
combobox3.pack  (fill = 'x', padx=2, side = 'left',pady=20)
labelDay1.pack  (fill = 'x', padx=2, side = 'left',pady=20)

labelBetween.pack(fill = 'x', padx=2, side = 'left',pady=20)

combobox4.pack  (fill = 'x', padx=2, side = 'left',pady=20)
labelYear2.pack (fill = 'x', padx=2, side = 'left',pady=20)
combobox5.pack  (fill = 'x', padx=2, side = 'left',pady=20)
labelMonth2.pack(fill = 'x', padx=2, side = 'left',pady=20)
combobox6.pack  (fill = 'x', padx=2, side = 'left',pady=20)
labelDay2.pack  (fill = 'x', padx=2, side = 'left',pady=20)

button1.pack(fill = 'x', padx=2, side = 'left',pady=20)
button2.pack(fill = 'x', padx=2, side = 'left',pady=20)
root.mainloop()