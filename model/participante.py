from datetime import datetime
from xmlrpc.client import boolean
from model.pessoa import Pessoa

class Participante(Pessoa):

    def __init__(self, nome:str, cpf:int, endereco:str, nascimento:datetime, vacina:boolean, exame:datetime):
        super().__init__(nome, cpf, nascimento, endereco)
        self.__vacina = vacina
        self.__exame = exame

    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina:boolean):
        self.__vacina = vacina
        
    @property
    def exame(self):
        return self.__exame
    
    @exame.setter
    def exame(self, exame):
        self.__exame = exame