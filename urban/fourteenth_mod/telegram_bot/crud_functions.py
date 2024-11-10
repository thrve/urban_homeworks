import sqlite3
from typing import List, Tuple, Optional

from keyboards.keyboards import ButtonText


def initiate_db(db_name: str = 'products.db') -> None:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        image_path TEXT
    );
    """

    cursor.execute(create_table_query)
    connection.commit()
    connection.close()


def get_all_products(db_name: str = 'products.db') -> List[Tuple[Optional[int], str, Optional[str], int]]:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    select_query = 'SELECT * FROM Products;'
    cursor.execute(select_query)

    products = cursor.fetchall()
    connection.close()

    return products


# def products(db_name: str = 'products.db') -> None:
#     connection = sqlite3.connect(db_name)
#     cursor = connection.cursor()
#     prod_path = '/home/thrv/.playground/urban/urban/urban/fourteenth_mod/telegram_bot/images/prod_'
#     products_data = [
#         (ButtonText.product1, f'Описание: {ButtonText.product1}', 100, f'{prod_path}1.jpg'),
#         (ButtonText.product2, f'Описание: {ButtonText.product2}', 200, f'{prod_path}2.jpg'),
#         (ButtonText.product3, f'Описание: {ButtonText.product3}', 300, f'{prod_path}3.jpg'),
#         (ButtonText.product4, f'Описание: {ButtonText.product4}', 400, f'{prod_path}4.jpg'),
#     ]
#
#     insert_query = 'INSERT INTO Products (title, description, price, image_path) VALUES (?, ?, ?, ?);'
#
#     cursor.executemany(insert_query, products_data)
#     connection.commit()
#     connection.close()


# initiate_db()
# products()
