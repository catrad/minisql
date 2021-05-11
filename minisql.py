"""
MINISQL V2.0 BY R
Новая версия построена на класах, сделано удобнее все параметры. Я не расписал всё это потому, что мне лень :)
"""

import sqlite3
import traceback
import sys

def raise_error(err):
	print(f"ERROR OCCURRED IN MINISQL!\nError: {err}")

class Database:
	def __init__(self, db, table=None):
		try:
			self.db = db
			if table != None:
				self.table = table
			else:
				self.table = None
		except:
			pass
	def table(self, table):
		if self.db != None:
			try:
				self.table = table
				return(True)
			except:
				return(False)
		else:
			raise_error("NO DATABASE!")
	def add(self, keys, values):
		if self.table != None:
			try:
			    sqlite_connection = sqlite3.connect(self.db)
			    cursor = sqlite_connection.cursor()
			    sqlite_insert_query = """INSERT INTO %s
			                          %s VALUES %s""" % (self.table, keys, values)
			    count = cursor.execute(sqlite_insert_query)
			    sqlite_connection.commit()
			    cursor.close()
			    return(True)
			except sqlite3.Error as error:
			    print("Не удалось вставить данные в таблицу sqlite")
			    print("Класс исключения: ", error.__class__)
			    print("Исключение", error.args)
			    print("Печать подробноcтей исключения SQLite: ")
			    exc_type, exc_value, exc_tb = sys.exc_info()
			    print(traceback.format_exception(exc_type, exc_value, exc_tb))
			    return(False)
			finally:
			    if (sqlite_connection):
			        sqlite_connection.close()
		else:
			raise_error("NO TABLE")

	def read(self):
		if self.table != None:
			try:
				sqlite_connection = sqlite3.connect(self.db)
				cursor = sqlite_connection.cursor()
				cursor.execute(f"SELECT * FROM {self.table}")
				results = cursor.fetchall() 
				sqlite_connection.commit()
				cursor.close()
				return results
			except Exception as err:
				raise_error(err)
		else:
			raise_error("NO TABLE")

	def get(self, value, where, equal):
		if self.table != None:
			try:
				sqlite_connection = sqlite3.connect(self.db)
				cursor = sqlite_connection.cursor()
				cursor.execute(f"SELECT {value} FROM {self.table} WHERE {where}={equal}")
				results = cursor.fetchall() 
				sqlite_connection.commit()
				cursor.close()
				return results[0][0]
			except Exception as err:
				raise_error(err)
		else:
			raise_error("NO TABLE")

	def edit(self, value, new_index, where, equal):
		if self.table != None:
			try:
				sqlite_connection = sqlite3.connect(self.db)
				cursor = sqlite_connection.cursor()
				sql_update_query = """Update %s set %s = ? where %s = ?""" % (self.table, value, where)
				data = (new_index, equal)
				cursor.execute(sql_update_query, data)
				sqlite_connection.commit()
				return True
				cursor.close()
				if (sqlite_connection):
				    sqlite_connection.close()
			except Exception as err:
				raise_error(err)
		else:
			raise_error("NO TABLE")

	def sread(self, sort_by, sort_type='ASC'):
		if self.table != None:
			try:
				sqlite_connection = sqlite3.connect(self.db)
				cursor = sqlite_connection.cursor()
				cursor.execute(f"SELECT * FROM {self.table} ORDER BY {sort_by} {sort_type}")
				results = cursor.fetchall() 
				sqlite_connection.commit()
				cursor.close()
				return results
			except Exception as err:
				raise_error(err)
		else:
			raise_error("NO TABLE")

	def request(self, request):
		try:
			sqlite_connection = sqlite3.connect(self.db)
			cursor = sqlite_connection.cursor()
			cursor.execute(request)
			sqlite_connection.commit()
			cursor.close()
			return True
		except Exception as err:
			raise_error(err)
