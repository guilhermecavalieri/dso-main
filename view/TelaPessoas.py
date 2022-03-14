from datetime import datetime
from view.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPessoas(TelaAbstrata):

    
    def __init__(self):
        self.__window = None
        
    def init_components(self):
        sg.ChangeLookAndFeel("Reddit")
        
        layout = [
            [sg.Text("MENU PESSOAS", font=("Helvetica", 20))],
            [sg.Text("__________________________________________")],
            [sg.Text("PARTICIPANTES")],
            [sg.Table(values=[["joao", "123"],["mathias","456"]], 
                    headings=["NOME", "CPF"], 
                    justification="center", 
                    expand_x=True, 
                    expand_y=True)],
            [sg.Button("Adicionar", key="bt_adicionar_participante"), 
            sg.Button("Alterar", key="bt_alterar_participante"), 
            sg.Button("Excluir", key="bt_excluir_participante")],
            [sg.Text("__________________________________________")],
            [sg.Text("ORGANIZADORES")],
            [sg.Table(values=[["joao", "123"],["mathias","456"]],
                    headings=["NOME", "CPF"], 
                    justification="center", 
                    expand_x=True, 
                    expand_y=True)],
            [sg.Button("Adicionar", key="bt_adicionar_organizador"), 
            sg.Button("Alterar", key="bt_alterar_organizador"), 
            sg.Button("Excluir", key="bt_excluir_organizador")],
            [sg.Text("", size=(1,1))],
            [sg.Submit("Voltar ao menu", key="bt_voltar_menu_principal", size=(45))]
                ]
        
        self.__window = sg.Window("Gerenciador de eventos", element_justification="c").Layout(layout)

    def open(self):
        self.init_components()
        event, values = self.__window.Read()
        return event
    
    def close(self):
        self.__window.Close()