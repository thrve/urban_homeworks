import sqlite3


with sqlite3.connect('not_telegram.db') as conn:
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
    """)

    users = []
    for i in range(1, 11):
        username = f'User  {i}'
        email = f'example{i}@gmail.com'
        age = i * 10
        balance = 1000
        users.append((username, email, age, balance))

    cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)

    cursor.execute('UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1')

    cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

    cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
    results = cursor.fetchall()

    for row in results:
        print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')
