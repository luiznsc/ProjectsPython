import json
import sqlalchemy
import cx_Oracle

from sqlalchemy import Column, Integer, String, Identity
from sqlalchemy.orm import sessionmaker

with open("./db_oracle.json", "r") as file:
    db_variables = json.load(file)

cx_Oracle.init_oracle_client(db_variables["oracle_client_path"])
username = db_variables["username"]
password = db_variables["password"]
server = db_variables["server"]
port = db_variables["port"]
dbname = db_variables["dbname"]

engine = sqlalchemy.create_engine(f"oracle+cx_oracle://{username}:{password}@{server}:{port}/{dbname}?encoding=UTF-8&nencoding=UTF-8")

# Cria uma sessÃ£o com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Cria uma classe para representar uma tabela no banco de dados
Base = sqlalchemy.orm.declarative_base()


class Pessoa(Base):
    __tablename__ = 'cp_pessoa_teste'

    id = Column(Integer, Identity(start=1), primary_key=True)
    nome = Column(String(50))
    idade = Column(Integer)

    def __repr__(self):
        return f"<Pessoa(nome='{self.nome}', idade={self.idade})>"

# Cria a tabela no banco de dados
Base.metadata.create_all(engine)

# Insere uma pessoa na tabela
pessoa1 = Pessoa(nome='JoÃ£o', idade=30)
felipe = Pessoa(nome="Felipe", idade=29)
mario = Pessoa(nome="Mario", idade=30)
session.add(pessoa1)
session.add(felipe)
session.add(mario)
session.commit()

# Seleciona todas as pessoas na tabela
pessoas = session.query(Pessoa).all()
print(pessoas)