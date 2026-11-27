from contextlib import contextmanager

import mysql.connector
from config import Config


class Database:
    def connect_mysql(self):
        conn = mysql.connector.connect(
            host=Config.MySQL_host, user=Config.MySQL_user,
            password=Config.MySQL_password, database=Config.MySQL_database,
        )
        return conn, conn.cursor()

    @contextmanager
    def cursor(self, write=False):
        conn, cursor = self.connect_mysql()
        try:
            yield cursor
            if write:
                conn.commit()
        except Exception:
            if write:
                conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def get_data(self, select_query, params=None):
        with self.cursor() as cursor:
            cursor.execute(select_query, params)
            return cursor.fetchall()

    def get_data_to_dict(self, select_query, params=None):
        with self.cursor() as cursor:
            cursor.execute(select_query, params)
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def create_table(self, create_query):
        with self.cursor(write=True) as cursor:
            cursor.execute(create_query)

    def insert_data(self, insert_query, params=None):
        with self.cursor(write=True) as cursor:
            cursor.execute(insert_query, params)

    def update_data(self, update_query, params=None):
        with self.cursor(write=True) as cursor:
            cursor.execute(update_query, params)
