import datetime

# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающа€ способ соединени€ с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

class Athelete(Base):
    """
    ќписывает структуру таблицы Athelete
    """
    # задаем название таблицы
    __tablename__ = 'athelete'

    # идентификатор, первичный ключ
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # возраст
    age = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # дата рождени€
    birthdate = sa.Column(sa.Text)
    # пол
    gender = sa.Column(sa.Text)
    # рост
    height = sa.Column(sa.Float)
    # им€
    name = sa.Column(sa.Text)
    # вес
    weight = sa.Column(sa.Integer)
    # золотые медали
    gold_medals = sa.Column(sa.Integer)
    # серебр€ные медали
    silver_medals = sa.Column(sa.Integer)
    # бронзовые медали
    bronze_medals = sa.Column(sa.Integer)
    # всего медалей
    total_medals = sa.Column(sa.Integer)
    # спорт
    sport = sa.Column(sa.Text)
    # страна
    country = sa.Column(sa.Text) 

class User(Base):
    """
    ќписывает структуру таблицы user дл€ хранени€ регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'user'

    # идентификатор пользовател€, первичный ключ
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # им€ пользовател€
    first_name = sa.Column(sa.Text)
    # фамили€ пользовател€
    last_name = sa.Column(sa.Text)
    # пол
    gender = sa.Column(sa.Text)
    # адрес электронной почты пользовател€
    email = sa.Column(sa.Text)
    # дата рождени€ пользовател€
    birthdate = sa.Column(sa.Text)
    # дата рождени€ пользовател€
    height = sa.Column(sa.Float)

def connect_db():
    """
    ”станавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def main():
    """
    ќсуществл€ет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()
    atheletes = session.query(Athelete).all()
    users = session.query(User).all()
    flag = 0
    id_user = int(input("¬ведите id пользовател€: "))
    find_user = session.query(User).filter(User.id == int(id_user)).first()
    if find_user:
        print("ƒата рождени€ пользовател€", find_user.birthdate)

        date_user = datetime.datetime.strptime(find_user.birthdate,'%Y-%m-%d')
    #ѕоиск атлета с такой же или ближайшей датой рождени€
        min_dif = 36000
        for athelete in atheletes:
            athelete_date = datetime.datetime.strptime(athelete.birthdate,'%Y-%m-%d')
            if athelete_date == date_user:
                print ("Ќайден атлет с такой же датой рождени€", athelete.id, athelete.name, athelete.birthdate)
                flag = 1
                break
            dif_date = date_user - athelete_date
            dd=str(dif_date)
            yy = dd.split()[0]
            xx=int(yy)
            dif = abs(xx)
            if dif < min_dif:
                min_dif=dif
                at_id = athelete.id
        if flag == 0:
            print ("Ќайден атлет с ближайшей датой рождени€:", at_id-1, atheletes[at_id-1].name, atheletes[at_id-1].birthdate)
    
    #ѕоиск атлета с таким же или ближайшим ростом
        find_at_h = session.query(Athelete).filter(Athelete.height == find_user.height).first()
        if find_at_h:
            print ("Ќайден атлет с таким же ростом", find_at_h.id, find_at_h.name, find_at_h.height)
        else:
            min_dif_h = 1
            at_id = 0
            for athelete in atheletes:
                if athelete.height:
                    dif = abs(athelete.height - find_user.height)
                    if dif < min_dif_h:
                        min_dif_h=dif
                        at_id = athelete.id
            print ("Ќайден атлет с ближайшим ростом", atheletes[at_id-1].id, atheletes[at_id-1].name, atheletes[at_id-1].height)
    else:
        print ("ѕользователь с таким id не найден в таблице")

if __name__ == "__main__":
    main()