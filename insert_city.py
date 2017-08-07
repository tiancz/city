import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://tian:123456@112.74.32.54:3306/tian?charset=utf8'

engine = create_engine(SQLALCHEMY_DATABASE_URI,echo=True)

DB_Session = sessionmaker(bind=engine)

session = DB_Session()

def insert(city_code,city_name):
#	sql = "insert into city_info(city_code,city_name)value('1001','tian')"
	sql = "insert into city_info(city_code,city_name)value("+"'"+city_code+"','"+city_name+"')"

	session.execute(sql)

	session.commit()

