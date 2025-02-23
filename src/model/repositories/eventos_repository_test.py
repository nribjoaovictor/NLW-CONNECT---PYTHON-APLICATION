import pytest 
from .eventos_repository import EventosRepository

@pytest.mark.skip("insert in DB")
def test_insert_eventos():
    event_name="eventoTeste2"
    event_repo=EventosRepository()

    event_repo.insert(event_name)

@pytest.mark.skip("select in DB")
def test_select_event():
    event_name="eventoTeste2"
    event_repo=EventosRepository()

    evento = event_repo.select_event(event_name)
    print(evento)
    print(evento.nome)
    print(evento.id)