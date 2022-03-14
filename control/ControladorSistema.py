from view.TelaSistema import TelaSistema
from control.ControladorEventos import ControladorEventos
from control.ControladorPessoas import ControladorPessoas

class ControladorSistema:

    def __init__(self):
        self.__controlador_eventos = ControladorEventos(self)
        self.__controlador_pessoas = ControladorPessoas(self)
        self.__tela_sistema = TelaSistema()

    def abre_eventos(self):
        self.__tela_sistema.close()
        self.__controlador_eventos.menu_eventos()

    def abre_participantes(self):
        self.__tela_sistema.close()
        self.__controlador_pessoas.menu_pessoas()

    def sair(self):
        exit(0)

    def menu_principal(self):
        lista_opcoes = {"bt_eventos": self.abre_eventos, "bt_participantes": self.abre_participantes, "bt_sair": self.sair}

        opcao_escolhida = self.__tela_sistema.open()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()
    
    def pegar_evento_por_titulo(self, titulo):
        
        if self.__controlador_eventos.eventos:
            for evento in self.__controlador_eventos.eventos:
                if evento.titulo == titulo:
                    return evento
            return None