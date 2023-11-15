import sqlite3 as sq

def sqlite_start():
    global conn, cursor
    
    conn = sq.connect("user_db.db")
    cursor = conn.cursor()
    
    conn.execute("CREATE TABLE IF NOT EXISTS users(login TEXT PRIMARY KEY, password TEXT)")
    conn.commit()
    
def sqlite_add_user(name: str, password: str) -> None:
    cursor.execute("INSERT INTO users(login, password) VALUES(?, ?)", (name, password))
    conn.commit()
    
def user_check_db(check_name: str) -> bool:
    user = cursor.execute("SELECT * FROM users WHERE login=?", (check_name,))
    return user.fetchone()

def password_check_db(user_name: str, password: str) -> None:
    is_correctly = cursor.execute("SELECT password FROM users WHERE login=?", (user_name,))
    return is_correctly.fetchone()

def register_user() -> None:
    login = input("Придумайте уникальный логин: ")
    if user_check_db(login):
        print('Извините, но данный логин занят!')
        return
    password = input("Придумайте надежный пароль: ")
    
    sqlite_add_user(login, password)
    print(f'{login} Вы успешно зарегистрировались')
    
def login_user() -> None:
    login = input("Введите свой логин от аккаунта: ")
    
    if user_check_db(login):
        password = input("Введите пароль от данного аккаунта: ")
        check_pass = password_check_db(login, password)
        
        if check_pass[0] == password:
            print('Пароль верен')
        else:
            print('Пароль неверен')
            return
    
sqlite_start()

while True:
    login_user()