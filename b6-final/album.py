import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """

    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums

def find_al(album_data):
    """
    Проверяем, есть ли в уже в БД альбом, данные которого ввели через POST запрос
    """
    session = connect_db()
    # проверяем альбом по названию, году и исполнителю. Жанр не проверяем, т.к. жанр могут написать по-разному
    find_album = session.query(Album).filter(Album.album == album_data["album"]).filter(Album.artist == album_data["artist"]).filter(Album.year == album_data["year"]).first()
    return find_album
    
def new_al(album_data):
    """
   Добавление нового альбома
    """
    session = connect_db()
    al_new = Album(year=album_data["year"], artist=album_data["artist"], genre=album_data["genre"], album=album_data["album"])
    session.add(al_new)
    session.commit()
    string1 = "Данные об альбоме успешно записаны в БД"
    return string1
    
    
    

