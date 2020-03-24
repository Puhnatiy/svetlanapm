import datetime
# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'user'

    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # имя пользователя
    first_name = sa.Column(sa.Text)
    # фамилия пользователя
    last_name = sa.Column(sa.Text)
    # пол пользователя
    gender = sa.Column(sa.Text)
    # адрес электронной почты пользователя
    email = sa.Column(sa.Text)
    # дата рождения пользователя
    birthdate = sa.Column(sa.Text)
    # рост пользователя
    height = sa.Column(sa.Float)

def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def request_data():
    """
    Запрашивает у пользователя данные и возвращает пользователя
    """
    # выводим приветствие
    print("Введите данные пользователя")
    # запрос данных
    first_name = input("Введите имя: ")
    last_name = input("А теперь фамилию: ")
    gender = input("Введите пол: ")
    email = input("Введите email: ")
    birthdate = input("Введите дату рождения в формате год-месяц-день, например 1985-02-27: ")
    height = input("Введите рост в метрах, разделитель - точка. Пример: 1.75: ")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=float(height)  
    )
    # возвращаем созданного пользователя
    return user

def main():
    """
    Основная функция. Вызывает функцию соединения с БД, запрашивает данные пользователя, записывает данные поьзователя в таблицу БД
    """
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    prodolzhit = ''
    prodolzhit = input ("Для регистрации следующего пользователя введите любой символ. Для завершения регистрации пользователей нажмите '2'")
    while prodolzhit != '2':
        user = request_data()
        session.add(user)
        session.commit()
        prodolzhit = input ("Для регистрации следующего пользователя введите любой символ. Для завершения регистрации пользователей нажмите '2'")

if __name__ == "__main__":
    main()