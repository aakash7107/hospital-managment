import mysql.connector

class Aakash:
    def __init__(self):
        self.my_connection = mysql.connector.connect(
            user='root', host='127.0.0.1', password='aakash', port=3306, database='aakash')
        self.my_cursor = self.my_connection.cursor()
    def iud(self, qry, values):
        try:
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def insert_with_id_return(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return self.my_cursor.lastrowid
    def insert_multiple_row(self, qry, values): #values is a list
        self.my_cursor.executemany(qry, values)
        self.my_connection.commit()
    def get_data(self, qry):
        try:
            self.my_cursor.execute(qry)
            data = self.my_cursor.fetchall()
            return data
        except Exception as e:
            print(e)

    def get_data_p(self, qry, values):
        self.my_cursor.execute(qry, values)
        data = self.my_cursor.fetchall()
        return data



# qry = "CREATE DATABASE cs19d"
# qry = "CREATE TABLE items (id int PRIMARY KEY AUTO_INCREMENT, name varchar(100), " \
#       "type varchar(100), price double)"
# qry = "INSERT INTO items (name, type, price) VALUES ('Burger', 'Chicken', 130)"
# my_cursor.execute(qry)
# my_connection.commit()
# qry = "SELECT * FROM items"
# my_cursor.execute(qry)
# all_items = my_cursor.fetchall()
# for i in all_items:
#     print(i)