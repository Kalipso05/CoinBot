import sqlite3
import logging

def sqlitedb_start():
    global conn, cursor
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    conn.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, money INTEGER)")
    conn.commit()
    
async def sqlile_add_user(user_id: int, money: int) -> None:
    """Функция добавляющая юзера в БД

    Args:
        user_id (int): tg id
        money (int): количество коинов выдаваемое новым юзерам
    """
    
    cursor.execute(f"INSERT INTO users(user_id, money) VALUES({user_id}, {money})")
    conn.commit()
    
async def sqlite_check_user(user_id: int) -> bool:
    """
    Функция проверяющая есть-ли юзер в базе данных

    Args:
        user_id (int): tg id юзера

    Returns:
        bool: возвращает значение если они есть в БД
    """
    
    user = cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
    return user.fetchone()
    

async def sqlite_add_money(count: int, user_id: int) -> None:
    
    """
    Функия позволяющая добавить юзеры коины
    """
    
    cursor.execute(f"UPDATE users SET money = money + {count} WHERE user_id= {user_id}")
    print(f'Пользователь с id: {user_id} получил {count} коинов')
    conn.commit()
    
async def sqlite_get_data(user_id: int, data: str) -> int:
    """Функция позволяющая получить значение каких-либо данных из БД

    Args:
        user_id (int): tg id\n
        data (str): Данные которые нужно получить

    Returns:
        int: value
    """
    
    value = cursor.execute(f"SELECT {data} from users WHERE user_id = {user_id}")
    return value.fetchone()