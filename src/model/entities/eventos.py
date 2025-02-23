from src.model.configs.base import base
from sqlalchemy import Column,String,Integer
class Eventos(base):
    __tablename__="Eventos"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nome= Column(String,nullable=False)
    