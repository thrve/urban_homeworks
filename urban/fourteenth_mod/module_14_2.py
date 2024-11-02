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
        username = f'User   {i}'
        email = f'example{i}@gmail.com'
        age = i * 10
        balance = 1000
        users.append((username, email, age, balance))

    cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)

    cursor.execute('DELETE FROM Users WHERE id = 6')

    cursor.execute('UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1')

    cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

    cursor.execute('SELECT COUNT(*) FROM Users')
    total_users = cursor.fetchone()[0]

    cursor.execute('SELECT SUM(balance) FROM Users')
    all_balances = cursor.fetchone()[0]

    if total_users > 0:
        average_balance = all_balances / total_users
    else:
        average_balance = 0

    print(average_balance)
