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
    


if __name__ == '__main__':
    #dbアクセス
    dbname    = 'TEST.db'
    conn      = dbAccess(dbname)
    field     = 'name'
    table     =  'persons'
    
    createSQL =  'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)'
    insertSQL = 'INSERT INTO persons(name) values("Taro")'
    selectSQL = 'SELECT * FROM persons'
    
    # sqliteを操作するカーソルオブジェクトを作成
    cur     = conn.cursor()
    connect = sqlite3.connect(dbname) 
    
    #dbCreateTable(createSQL)
    
    #レコード追加
    dbInsert(insertSQL)
    
    #セレクト文出力
    dbSelect(selectSQL)

    
    #コミット
    dbCommit()
    
    #クローズ
    dbClose()
    
    
    
    
    

    