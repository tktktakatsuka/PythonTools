from sqliteDAO import SqliteDAO

DB_NAME        = 'test01.sqlite3'
column_name    = 'name'
table_name     = 'yuutai'
value          = 'test'


sqlite_dao     = SqliteDAO(DB_NAME)
sqlite_dao       .create_table(column_name ,table_name)
sqlite_dao       .insert_data(value, table_name)
sqlite_dao       .connection_close()
