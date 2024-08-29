import os
import pyodbc
from  datetime import datetime,timezone
from flask import Flask ,request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

CREATE_t0 = (" CREATE TABLE kaall(id INT PRIMARY KEY, name TEXT);")
CREATE_ROOM = (" CREATE TABLE ball(id INT PRIMARY KEY, name TEXT);")
CREATE_t2 = (" CREATE TABLE IF NOT EXISTS temp(city_id INTEGER, tempreture REAL ,date TIMESTAMP, FOREIGN KEY(city_id) REFERENCES city(id) ON DELETE CASCADE );")


app = Flask(__name__)
load_dotenv()

server = os.getenv("SERVER")
db = os.getenv("DATABASE")
driver = os.getenv("DRIVER")
uid = os.getenv("USER")
pwd = os.getenv("PASSWORD")

for drivers in pyodbc.drivers():
    print(drivers)

# connection = pyodbc.connect('DRIVER='+ driver +';SERVER='+ server + ';DATABASE='+ db + ';UID='+ uid + ';PWD='+ pwd )
# connection = pyodbc.connect('DRIVER='+ driver +';SERVER='+ server + ';DATABASE='+ db + ';UID='+uid + ';PWD='+ pwd +';Trusted_Connection = yes; ')

# connection = pyodbc.connect(
#     'DRIVER={ODBC Driver 17 for SQL Server};'
#     'SERVER=' + server + ';'
#     'DATABASE=' + db + ';'
#     'UID=' + uid + ';'
#     'PWD=' + pwd + ';'
#     'TrustServerCertificate=yes;'
# )

connection = pyodbc.connect('DRIVER='+ driver +';SERVER='+ server + ';DATABASE='+ db +';Trusted_Connection = yes; ')
cursor = connection.cursor()
# cursor.execute(CREATE_t0)
# cursor.execute(CREATE_ROOM)
connection.commit()
cursor.close()
connection.close()

db2 = os.getenv("DATABASE2")
connection2 = pyodbc.connect('DRIVER='+ driver +';SERVER='+ server + ';DATABASE='+ db2 +';Trusted_Connection = yes; ')
cursor2 = connection2.cursor()
cursor2.execute("SELECT TOP(10) * FROM Person.Person")

for r in cursor2:
    print(r)
connection2.commit()
cursor2.close()
connection2.close()

# Queries
# CREATE_ROOM = (" CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);")
# CREATE_TEMP = (" CREATE TABLE IF NOT EXISTS temp(room_id INTEGER, tempreture REAL ,date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE );")
# INSERT_ROOM = ("INSERT INTO rooms (name) VALUES(%s) RETURNING id;")
# INSERT_TEMP = ("INSERT INTO temp(room_id,tempreture,date) VALUES(%s, %s, %s);")
# DAYS = ("SELECT COUNT(DISTINCT DATE(date)) AS days FROM temp;")
# AVG = ("SELECT AVG(tempreture) AS average FROM temp;")

# @app.post("/api/addall")
# def all():
#         data = request.get_json()
#         name = data["room_name"]
#         tempreture = data["tempreture"]
#
#         try:
#             date = datetime.strptime( data["date"], "%m-%d-%Y %H:%M:%S" )
#         except KeyError:
#             date = datetime.now( timezone.utc )
#
#         with connection:
#             with connection.cursor() as cursor:
#                 cursor.execute( CREATE_ROOM )
#                 cursor.execute( INSERT_ROOM, (name,) )
#                 room_id = cursor.fetchone()[0]
#
#                 cursor.execute( CREATE_TEMP )
#                 cursor.execute( INSERT_TEMP, (room_id, tempreture, date) )
#
#         return {"Room ID:": room_id, "message": f"Room : {name} with tempreture : {tempreture} added to database"}