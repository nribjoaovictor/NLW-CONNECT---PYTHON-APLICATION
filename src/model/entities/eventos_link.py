from src.model.configs.base import base
from sqlalchemy import Column,String,Integer, ForeignKey

class EventosLink(base):
    __tablename__="Eventos_link"
    id=Column(Integer,primary_key=True,autoincrement=True)
    
    evento_id=Column(Integer,ForeignKey("Eventos.id"))
    inscrito_id=Column(Integer,ForeignKey("inscritos.id"))
    link=Column(String,nullable=False)



