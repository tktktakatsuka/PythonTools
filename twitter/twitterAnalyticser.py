
import os
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

import datetime as dt
import tkinter as tk
import tkinter.ttk as ttk



def csvGrep(csv1,csv2,csv3,koumoku,year1,month1,day1,year2,month2,day2):
    print(os.getcwd())
    print(month2 )

    csvlist = []

    #TweetのデータをDataFrameに格納
    if csv1 != "":
        csvlist.append(pd.read_csv(csv1))
    if csv2 != "":
        csvlist.append(pd.read_csv(csv2))
    if csv3 != "":
        csvlist.append(pd.read_csv(csv3))


    
    #print(df_july.columns.values)
    tweets_df = pd.concat(csvlist)

    
    
    #表示させる列を選択する。
    greped_df = tweets_df[["Tweet text", "time","impressions","likes", "retweets", "replies" , "engagements" , "url clicks"]]

    #指定のカラムで降順で表示させる
    sorted_df = greped_df.sort_values(koumoku, ascending=False)

    #データフレーム追加（titleのみ）
    sorted_df['記事内のアフィリエイトリンクのクリック率']    = ''
    sorted_df['気をつけた事']                             = ''
    sorted_df['発生金額']                                 = ''

    #指定の範囲の時間で抽出する
    sorted_df["time"] = pd.to_datetime(sorted_df['time'] )
    sorted_df["time"] = sorted_df['time'].dt.strftime('%Y-%m-%d ')
    sorted_df["time"] = pd.to_datetime(sorted_df['time'])
    print(sorted_df.dtypes)

    #result_df = sorted_df.set_index(index=False)

    result_df =sorted_df[(sorted_df['time'] >= dt.datetime(int(year1),int(month1),int(day1))) & (sorted_df['time'] < dt.datetime(int(year2),int(month2),int(day2)))]
    #エクセルへ出力する。
    result_df.to_csv ('out.csv',encoding='cp932',index=False)
    print(result_df)
    # メッセージボックス（情報） 
    messagebox.showinfo('正常終了', '処理を終了します')



    



if __name__ == '__main__':

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
    frame4 = tk.Frame(root, pady=10, padx=10)

    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack()

    '''
    wigetの定義
    '''
    CsvFile    = tk.Label(frame1, text='①結合するCSVファイルの名を3つまで記入してください' , anchor='w' )
    file1 = tk.StringVar()
    entry1     = tk.Entry(frame1 , textvariable=file1)
    file2 = tk.StringVar()
    entry2     = tk.Entry(frame1 , textvariable=file2)
    file3 = tk.StringVar()
    entry3     = tk.Entry(frame1 , textvariable=file3) 



    grepPeriod    = tk.Label(frame2, text='②抽出期間を指定してください', anchor='w' )

    labelkoumoku    = tk.Label(frame3, text='③並び替え順の項目を選択してください', anchor='w')


    labelYear1    = tk.Label(frame2, text='年')
    labelMonth1   = tk.Label(frame2, text='月')
    labelDay1     = tk.Label(frame2, text='日')
    labelBetween  = tk.Label(frame2, text='～')
    labelYear2    = tk.Label(frame2, text='年')
    labelMonth2   = tk.Label(frame2, text='月')
    labelDay2     = tk.Label(frame2, text='日')



    #コンボボックス
    module = ["Tweet text", "time","impressions","likes", "retweets", "replies" , "engagements" , "url clicks"]
    koumoku = tk.StringVar()
    comboboxkoumoku = ttk.Combobox(frame3,values=module , height = 2, width = 20 , textvariable= koumoku, state="readonly" )


    module = ('2020', '2021', '2022', '2023', '2024', '2025')
    year1 = tk.IntVar()
    combobox1 = ttk.Combobox(frame2,values=module , height = 2, width = 6 , textvariable= year1, state="readonly" )
    
    module = ('1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12')
    month1 = tk.IntVar()
    combobox2 = ttk.Combobox(frame2,values=module , height = 2, width = 3, textvariable= month1, state="readonly")

    module = ('1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12','13', '14', '15', '16', '17', '18','19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30','31')
    day1 = tk.IntVar()
    combobox3 = ttk.Combobox(frame2,values=module , height = 2, width = 3,textvariable= day1, state="readonly")

    module = ('2020', '2021', '2022', '2023', '2024', '2025')
    year2 = tk.IntVar()
    combobox4 = ttk.Combobox(frame2,values=module ,height = 2, width = 6,textvariable= year2, state="readonly")
    
    module = ('1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12')
    month2 = tk.IntVar()
    combobox5 = ttk.Combobox(frame2,values=module , height = 2, width = 3,textvariable= month2, state="readonly")

    module = ('1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12','13', '14', '15', '16', '17', '18','19', '20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30','31')
    day2 = tk.IntVar()
    combobox6 = ttk.Combobox(frame2,values=module ,height = 2, width = 3,textvariable= day2, state="readonly")




    button1 = ttk.Button(frame4 , text='OK.'    ,command=lambda:csvGrep(file1.get(),file2.get(),file3.get(),koumoku.get(),year1.get(),month1.get(),day1.get(),year2.get(),month2.get(),day2.get()))
    button2 = ttk.Button(frame4 , text='Cancel.',command="")

    '''
    画面を配置する処理
    '''
    CsvFile.pack(fill = 'x', padx=2, side = 'top',pady=20)
    entry1.pack(fill = 'x', padx=5, side = 'left',pady=20)
    entry2.pack(fill = 'x', padx=5, side = 'left',pady=20)
    entry3.pack(fill = 'x', padx=5, side = 'left',pady=20,)




    grepPeriod.pack (fill = 'x', padx=2, side = 'top',pady=20)
    combobox1.pack  (fill = 'x', padx=2, side = 'left',pady=20)
    

    labelkoumoku.pack   (fill = 'x', padx=2,side = 'left',pady=20)
    comboboxkoumoku.pack(fill = 'x', padx=5,pady=20,)


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
