from model.pessoa import Pessoa
import datetime
class Evento:
    
    def __init__(self, titulo:str, data: datetime.datetime, local:str, capacidade_maxima:int):
        self.__titulo = titulo
        self.__data = data
        self.__local = local
        self.__capacidade_maxima = capacidade_maxima
        self.__organizadores = []
        self.__participantes = []
        self.__num_participantes = 0

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo:str):
        self.__titulo = titulo

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data:str):
        self.__data = data

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local:str):
        self.__local = local

    @property
    def capacidade_maxima(self):
        return self.__capacidade_maxima

    @capacidade_maxima.setter
    def capacidade_maxima(self, capacidade_maxima:int):
        self.__capacidade_maxima = capacidade_maxima

    @property
    def organizadores(self):
        return self.__organizadores

    @organizadores.setter
    def organizadores(self, organizadores: Pessoa):
        self.__organizadores = organizadores

    @property
    def participantes(self):
        return self.__participantes

    @participantes.setter
    def participantes(self, participantes: Pessoa):
        self.__participantes = participantes

    @property
    def num_participantes(self):
        return self.__num_participantes
    
    @num_participantes.setter
    def num_participantes(self, num_participantes):
        self.__num_participantes = num_participantes