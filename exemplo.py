from sqlalchemy import create_engine

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

# Antes de inserir ou consultar dados, precisamos definir os modelos e criar tabelas correspondentes no banco de dados:
print("Conexão com SQLite estabelecida.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

## Criar as tabelas no banco de dados
# Base.metadata.create_all(engine)

# Criando Sessões e Inserindo Dados
# As sessões no SQLAlchemy são usadas para manter um 'workspace' de 
# todas as operações de objetos que você deseja sincronizar com o banco de dados:
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome='João', idade=28)
session.add(novo_usuario)
session.commit()

print("Usuário inserido com sucesso.")