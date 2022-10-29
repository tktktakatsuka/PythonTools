import sqlite3
from unicodedata import name

# TEST.dbを作成する
# すでに存在していれば、それにアスセスする。
def dbAccess(dbname):
    connect = sqlite3.connect(dbname) 
    return connect

#テーブル作成
def createTable(createSQL):
    cur.execute(createSQL)

#レコード追加
def dbInsert(insertSQL):
    cur.execute(insertSQL)

#セレクト分
def dbSelect(selectSql):
    cur.execute(selectSql)
 
# データベースへコミット。    
def dbCommit():
    conn.commit
 
     
# データベースへのコネクションを閉じる。(必須)    
def dbClose():
    conn.close()
    


if __name__ == '__main__':
    #dbアクセス
    dbname    = 'TEST.db'
    conn      = dbAccess(dbname)
    createSQL = 'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)'
    
    # sqliteを操作するカーソルオブジェクトを作成
    cur     = conn.cursor()
    connect = sqlite3.connect(dbname) 
    createTable(createSQL)
    
    

    