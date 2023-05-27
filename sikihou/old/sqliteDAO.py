
import sqlite3


class SqliteDAO:
    #グローバル変数
    conn                  = ""
    cur                   = None
    
    """
    SQliteに接続するクラス
    Attributes:
        conn (属性の型):  connection
    """
    
    def __init__(self,dbName):
        """
        DBアクセスを実施する。
        Args:
            dbName (String): databaseの名前を格納            
        """
        self.conn         = sqlite3.connect(dbName) 
        self.cur          = self.conn.cursor()
        
    def create_table(self , column_name, table_name):
        """
        tableが存在しない場合、tableを作成する
        Args:
            arg1 (String): table名を格納         
        """
        if(self.cur != None):
            self.cur.execute(r'create table IF NOT EXISTS ' + table_name + '(' + str(column_name) + ')')
        
            
    def insert_data(self, value , table_name):
        """
        insertを実施する。
        Args:
            value (String): 値を格納    
            table_name    : テーブル名を格納 
        """
        try:
            sql           = f"INSERT INTO " + table_name + " (name) values (?)"     
            data          = [str(value)]
            self.cur.execute(sql, data)
            self.conn.commit()
        except sqlite3.IntegrityError:
            global uniqueCounter
            uniqueCounter = uniqueCounter +1 
            pass
        
            
    def connection_close(self):
        """
        dbコネクションを切断する
        Args:
        """
        self.conn.close()