from abc import ABC,abstractmethod
from src.model.entities.inscritos import inscritos

class SubscribersRepositoryInterface(ABC):
    @abstractmethod
    def insert(self,subscriber_infos:dict) -> None:
        pass
        
    @abstractmethod
    def select_subscriber(self,email:str,evento_id:int) -> inscritos:
        pass

    @abstractmethod
    def select_subscribers_by_link(self,link:str,event_id:int)->list: pass

    @abstractmethod
    def get_ranking(self,event_id:int)->list: pass
