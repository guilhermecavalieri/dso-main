from daos.DAOAbstrato import DAO
from model.evento import Evento
class DAOOrganizador(DAO):
    def __init__(self):
        super().__init__('organizadores.pkl')

    def add(self, organizador):
        super().add(organizador.nome, organizador)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key, 'Organizador')

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)