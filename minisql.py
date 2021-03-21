# minisql cursor.execute("SELECT balance FROM users WHERE user_id=?", (replyid,)).fetchall()
def add(baza, yach, value):
	import sqlite3
	import traceback
	import sys

	try:
	    sqlite_connection = sqlite3.connect(baza[0])
	    cursor = sqlite_connection.cursor()
	    sqlite_insert_query = """INSERT INTO %s
	                          %s VALUES  %s""" % (baza[1], yach, value)

	    count = cursor.execute(sqlite_insert_query)
	    sqlite_connection.commit()
	    cursor.close()

	except sqlite3.Error as error:
	    print("Не удалось вставить данные в таблицу sqlite")
	    print("Класс исключения: ", error.__class__)
	    print("Исключение", error.args)
	    print("Печать подробноcтей исключения SQLite: ")
	    exc_type, exc_value, exc_tb = sys.exc_info()
	    print(traceback.format_exception(exc_type, exc_value, exc_tb))
	finally:
	    if (sqlite_connection):
	        sqlite_connection.close()

def read(baza):
	import sqlite3
	sqlite_connection = sqlite3.connect(baza[0])
	cursor = sqlite_connection.cursor()
	cursor.execute(f"SELECT * FROM {baza[1]}")
	results = cursor.fetchall() 
	sqlite_connection.commit()
	cursor.close()
	return results

def get(baza, yach, key, key1):
	import sqlite3
	sqlite_connection = sqlite3.connect(baza[0])
	cursor = sqlite_connection.cursor()
	cursor.execute(f"SELECT {yach} FROM {baza[1]} WHERE {key}={key1}")
	results = cursor.fetchall() 
	sqlite_connection.commit()
	cursor.close()
	return results[0][0]

def edit(baza, yach, edit_to, key, key1):
	import sqlite3
	sqlite_connection = sqlite3.connect(baza[0])
	cursor = sqlite_connection.cursor()
	sql_update_query = """Update %s set %s = ? where %s = ?""" % (baza[1], yach, key)
	data = (edit_to, key1)
	cursor.execute(sql_update_query, data)
	sqlite_connection.commit()
	return True
	cursor.close()
	if (sqlite_connection):
	        sqlite_connection.close()


