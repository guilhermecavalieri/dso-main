from abc import ABC, abstractmethod
import PySimpleGUI as sg
from exceptions.IntervalError import IntervalError
from exceptions.LengthError import LengthError

class TelaAbstrata(ABC):

    @abstractmethod
    def __init__(self):
        pass
    
    def cria_input_de_string(self, mensagem, key, string_default):
        return sg.Text(mensagem, size=(18,0)), sg.InputText(string_default, key=key, do_not_clear=True, enable_events=True)
    
    def cria_input_de_data(self, mensagem, key1, key2, key3, dia_default, mes_default, ano_default):
        return sg.Text(mensagem, size=(18,0)), sg.InputText(dia_default, size=(12,0), key=key1, do_not_clear=True, enable_events=True), sg.Text("/"), sg.InputText(mes_default, size=(12,0), key=key2, do_not_clear=True, enable_events=True), sg.Text("/"), sg.InputText(ano_default, size=(12,0), key=key3, do_not_clear=True, enable_events=True)
    
    def cria_input_de_horario(self, mensagem, key1, key2, hora_default, minuto_default):
        return sg.Text(mensagem, size=(18,0)), sg.InputText(hora_default, size=(20,0), key=key1, do_not_clear=True, enable_events=True), sg.Text(": "), sg.InputText(minuto_default, size=(20,0), key=key2, do_not_clear=True, enable_events=True)

    def mostra_mensagem(self, mensagem):
        sg.Popup(mensagem)

