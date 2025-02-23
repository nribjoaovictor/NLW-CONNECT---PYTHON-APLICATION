from sqlalchemy import func,desc
from src.model.configs.connection import DBconnectionHandler
from src.model.entities.inscritos import inscritos
from .interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
    def insert(self,subscriber_infos:dict) -> None:
        with DBconnectionHandler() as db:
            try:
                new_subscriber= inscritos(
                    nome=subscriber_infos.get("name"),
                    email=subscriber_infos.get("email"),
                    link=subscriber_infos.get("link"),
                    evento_id=subscriber_infos.get("evento_id")
                )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
        
    def select_subscriber(self,email:str,evento_id:int) -> inscritos:
        with DBconnectionHandler() as db:
            data=(
                db.session
                .query(inscritos)
                .filter(
                    inscritos.email==email,
                    inscritos.evento_id == evento_id)
                .one_or_none()
            )
            return data
        
    def select_subscribers_by_link(self,link:str,event_id:int)->list:
        with DBconnectionHandler() as db:
            data=(
                db.session
                .query(inscritos)
                .filter(
                    inscritos.link==link,
                    inscritos.evento_id == event_id)
                .all()
            )
            return data
        
    def get_ranking(self,event_id:int)->list:
        with DBconnectionHandler() as db:
            result=(
                db.session
                .query(
                    inscritos.link,
                    func.count(inscritos.id).label("total")
                )
                .filter(
                    inscritos.evento_id==event_id,
                    inscritos.link.isnot(None)
                )
                .group_by(inscritos.link)
                .order_by(desc("total"))
                .all()
            ) 
            return result