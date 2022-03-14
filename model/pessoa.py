from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome:str, cpf:int, nascimento:str, endereco:str):
        self.__nome = nome
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__endereco = endereco
        self.__eventos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf:int):
        self.__cpf = cpf

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento:str):
        self.__nascimento = nascimento

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco:str):
        self.__endereco = endereco
        
    @property
    def eventos(self):
        return self.__eventos
    
    @eventos.setter
    def eventos(self, eventos):
        self.__eventos = eventos
