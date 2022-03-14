from model.pessoa import Pessoa

class Organizador(Pessoa):

    def __init__(self, nome, cpf):
        super().__init__(nome, cpf, None, None)