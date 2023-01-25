import sqlite3

connection = sqlite3.connect('taxibd.db')
sql = connection.cursor()
# Создать таблицу
connection = sqlite3.connect('taxibd.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS taxibd (user_id INT, clients TEXT, telephone TEXT)')
connection.commit()
connection.close()


# Функция регистарции
def registraton(user_id, name=0, user_number=0):
    connection = sqlite3.connect('taxibd.db')
    sql = connection.cursor()

    sql.execute(f'SELECT user_id FROM taxibd WHERE user_id = {user_id};')

    if not sql.fetchall():
        sql.execute(f'INSERT INTO taxibd (user_id, clients, telephone) VALUES ({user_id}, "{name}", "{user_number}");')
        connection.commit()
        return True

    else:
        return False