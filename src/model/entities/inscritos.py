from src.model.configs.base import base
from sqlalchemy import Column,String,Integer, ForeignKey

class inscritos(base):
    __tablename__="inscritos"
    id=Column(Integer,primary_key=True,autoincrement=True)
    nome=Column(String,nullable=False)
    email=Column(String,nullable=False)
    link=Column(String,nullable=True)
    evento_id=Column(Integer,ForeignKey("Eventos.id"))




