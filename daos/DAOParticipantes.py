from daos.DAOAbstrato import DAO

class DAOParticipante(DAO):
    def __init__(self):
        super().__init__('participantes.pkl')

    def add(self, participante):
        super().add(participante.nome, participante)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key, 'Organizador')

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)