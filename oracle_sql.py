import json
import cx_Oracle

with open("./db_oracle.json", "r") as file:
    db_variables = json.load(file)

cx_Oracle.init_oracle_client(db_variables["oracle_client_path"])
username = db_variables["username"]
password = db_variables["password"]
server = db_variables["server"]
port = db_variables["port"]
dbname = db_variables["dbname"]

dsn = cx_Oracle.makedsn(server, port, dbname)
connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)

with connection.cursor() as cursor:
    for row in cursor.execute("select * from CP_PESSOA_TESTE"):
        print(row)

connection.close()