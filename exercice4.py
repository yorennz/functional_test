import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        column_str = ', '.join([f'{col_name} {data_type}' for col_name, data_type in columns.items()])
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({column_str})'
        self.cursor.execute(query)

    def insert_into_table(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' * len(data))
        query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
        self.cursor.execute(query, tuple(data.values()))

    def select_from_table(self, table_name, columns="*", condition=None):
        query = f'SELECT {columns} FROM {table_name}'
        if condition:
            query += f' WHERE {condition}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_table(self, table_name, updated_data, condition):
        updated_str = ', '.join([f'{key} = ?' for key in updated_data.keys()])
        query = f'UPDATE {table_name} SET {updated_str} WHERE {condition}'
        self.cursor.execute(query, tuple(updated_data.values()))

    def delete_from_table(self, table_name, condition):
        query = f'DELETE FROM {table_name} WHERE {condition}'
        self.cursor.execute(query)

    def close_connection(self):
        self.conn.close()
