from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Fornecedores(Base):

    __tablename__ = 'Fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String,(20))
    email = Column(String(50))
    endereco = Column(String(100))

    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class Produto(Base):

    __tablename__ = 'produtos'
    id = (Column(Integer, primary_key=True))
    nome = Column(String(50, nullable=False))
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor = Column(Integer, ForeignKey ('fornecedores'))

    # Estabelece a relação entre produto e fornecedor
    fornecedor = relationship ("Fornecedor")

    engine = create_engine('sqlite:///:memory:',cecho=True)
    Base.metadata.create.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()