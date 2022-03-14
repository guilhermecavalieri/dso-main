from daos.DAOAbstrato import DAO
from model.evento import Evento
class DAOEvento(DAO):
    def __init__(self):
        super().__init__('eventos.pkl')

    def add(self, evento: Evento):
        if isinstance(evento.titulo, str) and evento is not None and isinstance(evento, Evento):
            super().add(evento.titulo, evento)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key, 'Evento')

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
