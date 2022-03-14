class Exame:

    def __init__(self, data:str):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data:str):
        self.__data = data