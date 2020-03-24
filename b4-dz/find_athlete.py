import datetime

# ����������� ���������� sqlalchemy � ��������� ������� �� ��� 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ���������, ����������� ������ ���������� � ����� ������
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# ������� ����� ������� ������
Base = declarative_base()

class Athelete(Base):
    """
    ��������� ��������� ������� Athelete
    """
    # ������ �������� �������
    __tablename__ = 'athelete'

    # �������������, ��������� ����
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # �������
    age = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # ���� ��������
    birthdate = sa.Column(sa.Text)
    # ���
    gender = sa.Column(sa.Text)
    # ����
    height = sa.Column(sa.Float)
    # ���
    name = sa.Column(sa.Text)
    # ���
    weight = sa.Column(sa.Integer)
    # ������� ������
    gold_medals = sa.Column(sa.Integer)
    # ���������� ������
    silver_medals = sa.Column(sa.Integer)
    # ��������� ������
    bronze_medals = sa.Column(sa.Integer)
    # ����� �������
    total_medals = sa.Column(sa.Integer)
    # �����
    sport = sa.Column(sa.Text)
    # ������
    country = sa.Column(sa.Text) 

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
    # ���
    gender = sa.Column(sa.Text)
    # ����� ����������� ����� ������������
    email = sa.Column(sa.Text)
    # ���� �������� ������������
    birthdate = sa.Column(sa.Text)
    # ���� �������� ������������
    height = sa.Column(sa.Float)

def connect_db():
    """
    ������������� ���������� � ���� ������, ������� �������, ���� �� ��� ��� � ���������� ������ ������ 
    """
    # ������� ���������� � ���� ������
    engine = sa.create_engine(DB_PATH)
    # ������� ������� ������
    session = sessionmaker(engine)
    # ���������� ������
    return session()

def main():
    """
    ������������ �������������� � �������������, ������������ ���������������� ����
    """
    session = connect_db()
    atheletes = session.query(Athelete).all()
    users = session.query(User).all()
    flag = 0
    id_user = int(input("������� id ������������: "))
    find_user = session.query(User).filter(User.id == int(id_user)).first()
    if find_user:
        print("���� �������� ������������", find_user.birthdate)

        date_user = datetime.datetime.strptime(find_user.birthdate,'%Y-%m-%d')
    #����� ������ � ����� �� ��� ��������� ����� ��������
        min_dif = 36000
        for athelete in atheletes:
            athelete_date = datetime.datetime.strptime(athelete.birthdate,'%Y-%m-%d')
            if athelete_date == date_user:
                print ("������ ����� � ����� �� ����� ��������", athelete.id, athelete.name, athelete.birthdate)
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
            print ("������ ����� � ��������� ����� ��������:", at_id-1, atheletes[at_id-1].name, atheletes[at_id-1].birthdate)
    
    #����� ������ � ����� �� ��� ��������� ������
        find_at_h = session.query(Athelete).filter(Athelete.height == find_user.height).first()
        if find_at_h:
            print ("������ ����� � ����� �� ������", find_at_h.id, find_at_h.name, find_at_h.height)
        else:
            min_dif_h = 1
            at_id = 0
            for athelete in atheletes:
                if athelete.height:
                    dif = abs(athelete.height - find_user.height)
                    if dif < min_dif_h:
                        min_dif_h=dif
                        at_id = athelete.id
            print ("������ ����� � ��������� ������", atheletes[at_id-1].id, atheletes[at_id-1].name, atheletes[at_id-1].height)
    else:
        print ("������������ � ����� id �� ������ � �������")

if __name__ == "__main__":
    main()