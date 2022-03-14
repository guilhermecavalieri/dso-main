from abc import ABC, abstractmethod
import PySimpleGUI as sg
from exceptions.IntervalError import IntervalError
from exceptions.LengthError import LengthError

class TelaAbstrata(ABC):

    @abstractmethod
    def __init__(self):
        pass
    
    def cria_input_de_string(self, mensagem, key):
        return sg.Text(mensagem, size=(18,0)), sg.InputText(key=key, do_not_clear=True, enable_events=True)
    
    def cria_input_de_data(self, mensagem, key1, key2, key3):
        return sg.Text(mensagem, size=(18,0)), sg.InputText(size=(12,0), key=key1, do_not_clear=True, enable_events=True), sg.Text("/"), sg.InputText(size=(12,0), key=key2, do_not_clear=True, enable_events=True), sg.Text("/"), sg.InputText(size=(12,0), key=key3, do_not_clear=True, enable_events=True)
    
    def cria_input_de_horario(self, mensagem, key1, key2):
        return sg.Text(mensagem, size=(18,0)), sg.InputText(size=(20,0), key=key1, do_not_clear=True, enable_events=True), sg.Text(": "), sg.InputText(size=(20,0), key=key2, do_not_clear=True, enable_events=True)

    def mostra_mensagem(self, mensagem):
        sg.Popup(mensagem)

    def le_opcao_escolhida(self, inteiros_validos: list = None):

        while True:

            string = input()
            try:    
                if not string:
                    raise EOFError
                inteiro = int(string)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
            except ValueError:
                print("Valor incorreto")
            except EOFError:
                print("Valor não pode estar vazio")
            else:
                return inteiro

    def le_data(self, mensagem):

        while True:
            try:
                string = input(mensagem)
                if not string:
                    raise EOFError
                if (string[0:2].isnumeric() and int(string[0:2]) <= 28) and string[2] == "/" and (string[3:5].isnumeric() and int(string[3:5]) <= 12) and string[5] == "/" and string[6:].isnumeric():
                    dia = int(string[0:2])
                    mes = int(string[3:5])
                    ano = int(string[6:])
                    return dia, mes, ano
                else:
                    raise TypeError
            except IndexError:
                print("O formato da data está errado")
            except TypeError:
                print("O formato da data está errado")
            except EOFError:
                print("A data não pode estar vazio")


    def le_hora(self):

        while True:
            try:
                string = input("Horário formato hh:mm: ")
                if not string:
                    raise EOFError
                if string[0:2].isnumeric() and string[2] == ":" and string[3:5].isnumeric() and len(string) == 5:
                    hora = int(string[0:2])
                    minuto = int(string[3:])
                    return hora, minuto
                else:
                    raise TypeError
            except IndexError:
                print("O formato da hora está errado")
            except TypeError:
                print("O formato da hora está errado")
            except EOFError:
                print("O horário não pode estar vazio")
                
    def le_nome(self):
        while True:
            try:
                string = input("Nome: ")
                if not string:
                    raise EOFError
                if len(string) > 30 or not string.isalpha():
                    raise TypeError
                return string
            except EOFError:
                print("Não pode estar vazio")
            except TypeError:
                print("Não pode ter mais de 30 caracteres")

    def le_numero_inteiro(self, mensagem:str, numero_maximo:int, numero_minimo):

        while True:
            try:
                numero = input(mensagem)
                if not numero:
                    raise EOFError
                numero = int(numero)
                if numero > numero_maximo or numero < numero_minimo:
                    raise IntervalError
                return numero
            except IntervalError:
                print("Somente números acima de ", numero_minimo)
            except ValueError:
                print("Valor incorreto. Digite apenas números inteiros")
            except EOFError:
                print("O valor não pode estar vazia")

    def limpa_tela(self):
        for _ in range(50):
            print()
            
    def le_cpf(self):

        while True:
            try:
                string = input("CPF formato XXX.XXX.XXX-XX: ")
                if not string:
                    raise EOFError
                if string[0:3].isnumeric() and string[3] == "." and string[4:7].isnumeric() and string[7] == "." and string[8:11].isnumeric and string[11] == "-" and string[12:].isnumeric:
                    return string
                else:
                    raise TypeError
            except EOFError:
                print("CPF não pode ficar vazio")
            except TypeError:
                print("CPF inválido")
