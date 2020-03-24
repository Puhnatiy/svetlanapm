import datetime
# ����������� ���������� sqlalchemy � ��������� ������� �� ��� 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ���������, ����������� ������ ���������� � ����� ������
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# ������� ����� ������� ������
Base = declarative_base()

class User(Base):
    """
    ��������� ��������� ������� user ��� �������� ��������������� ������ �������������
    """
    # ������ �������� �������
    __tablename__ = 'user'

    # ������������� ������������, ��������� ����
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # ��� ������������
    first_name = sa.Column(sa.Text)
    # ������� ������������
    last_name = sa.Column(sa.Text)
    # ��� ������������
    gender = sa.Column(sa.Text)
    # ����� ����������� ����� ������������
    email = sa.Column(sa.Text)
    # ���� �������� ������������
    birthdate = sa.Column(sa.Text)
    # ���� ������������
    height = sa.Column(sa.Float)

def connect_db():
    """
    ������������� ���������� � ���� ������, ������� �������, ���� �� ��� ��� � ���������� ������ ������ 
    """
    # ������� ���������� � ���� ������
    engine = sa.create_engine(DB_PATH)
    # ������� ��������� �������
    Base.metadata.create_all(engine)
    # ������� ������� ������
    session = sessionmaker(engine)
    # ���������� ������
    return session()

def request_data():
    """
    ����������� � ������������ ������ � ���������� ������������
    """
    # ������� �����������
    print("������� ������ ������������")
    # ������ ������
    first_name = input("������� ���: ")
    last_name = input("� ������ �������: ")
    gender = input("������� ���: ")
    email = input("������� email: ")
    birthdate = input("������� ���� �������� � ������� ���-�����-����, �������� 1985-02-27: ")
    height = input("������� ���� � ������, ����������� - �����. ������: 1.75: ")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=float(height)  
    )
    # ���������� ���������� ������������
    return user

def main():
    """
    �������� �������. �������� ������� ���������� � ��, ����������� ������ ������������, ���������� ������ ����������� � ������� ��
    """
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    prodolzhit = ''
    prodolzhit = input ("��� ����������� ���������� ������������ ������� ����� ������. ��� ���������� ����������� ������������� ������� '2'")
    while prodolzhit != '2':
        user = request_data()
        session.add(user)
        session.commit()
        prodolzhit = input ("��� ����������� ���������� ������������ ������� ����� ������. ��� ���������� ����������� ������������� ������� '2'")

if __name__ == "__main__":
    main()